CREATE TABLE IF NOT EXISTS users {
    UserID Integer PRIMARY KEY,
    PermID Integer DEFAULT 0
}

CREATE TABLE IF NOT EXISTS designated_channels {
    ServerID Integer PRIMARY KEY,
}