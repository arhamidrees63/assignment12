# app/auth/redis.py
import redis.asyncio as aioredis
from app.core.config import get_settings

settings = get_settings()

# Re-use a single async Redis connection
_redis_instance = None


async def get_redis():
    """Return a global Redis connection (async)."""
    global _redis_instance
    if _redis_instance is None:
        _redis_instance = aioredis.from_url(
            settings.REDIS_URL or "redis://localhost:6379",
            encoding="utf-8",
            decode_responses=True,
        )
    return _redis_instance


async def add_to_blacklist(jti: str, exp: int):
    """Add a token’s JTI to the blacklist with expiration."""
    redis = await get_redis()
    await redis.set(f"blacklist:{jti}", "1", ex=exp)


async def is_blacklisted(jti: str) -> bool:
    """Check if a token’s JTI is blacklisted."""
    redis = await get_redis()
    return await redis.exists(f"blacklist:{jti}") == 1
