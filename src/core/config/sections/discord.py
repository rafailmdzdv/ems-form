from dataclasses import dataclass


@dataclass(frozen=True)
class DiscordSection:
    token: str
    role_id: int
