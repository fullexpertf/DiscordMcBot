-- Initial database schema
CREATE TABLE IF NOT EXISTS guild_configs (
    id INTEGER PRIMARY KEY,
    language TEXT DEFAULT 'en',
    prefixes TEXT,
    welcome_channel_id INTEGER,
    goodbye_channel_id INTEGER,
    autorole_id INTEGER,
    starboard_channel_id INTEGER,
    star_threshold INTEGER DEFAULT 5,
    xp_enabled INTEGER DEFAULT 1,
    xp_rate INTEGER DEFAULT 1,
    economy_currency TEXT DEFAULT '₺',
    muted_role_id INTEGER,
    automod_badwords TEXT,
    automod_caps_threshold INTEGER DEFAULT 0,
    automod_links INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS user_profiles (
    user_id INTEGER,
    guild_id INTEGER,
    xp INTEGER DEFAULT 0,
    level INTEGER DEFAULT 0,
    reputation INTEGER DEFAULT 0,
    wallet INTEGER DEFAULT 0,
    bank INTEGER DEFAULT 0,
    last_message_at TIMESTAMP,
    PRIMARY KEY (user_id, guild_id)
);

CREATE TABLE IF NOT EXISTS infractions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    guild_id INTEGER,
    type TEXT,
    reason TEXT,
    moderator_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    guild_id INTEGER,
    opener_id INTEGER,
    channel_id INTEGER,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    closed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reaction_roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    guild_id INTEGER,
    message_id INTEGER,
    emoji TEXT,
    role_id INTEGER
);
