CREATE TABLE "user" (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    bachelor_degree VARCHAR(255),
    posX FLOAT,
    posY FLOAT
);

CREATE TABLE "class" (
    id UUID PRIMARY KEY,
    type VARCHAR(255),
    name VARCHAR(255),
    time_frame TIMESTAMP,
    day DATE
);

CREATE TABLE "room" (
    id UUID PRIMARY KEY,
    name VARCHAR(255),
    posX FLOAT,
    posY FLOAT
);

CREATE TABLE "checkpoint" (
    id UUID PRIMARY KEY,
    name VARCHAR(255),
    posX FLOAT,
    posY FLOAT,
    NFCtag UUID,
    description TEXT,
    radius DOUBLE PRECISION
);

CREATE TABLE "tempRoute" (
    id UUID PRIMARY KEY,
    posX FLOAT,
    posY FLOAT,
    status VARCHAR(255),
    startTimeframe TIMESTAMP,
    endTimeframe TIMESTAMP
);

CREATE TABLE "tempCheckpoint" (
    id UUID PRIMARY KEY,
    order_num INT,
    scanned BOOLEAN,
    scanTimeframe TIMESTAMP,
    checkpoint_id UUID NOT NULL REFERENCES "checkpoint"(id),
    tempRoute_id UUID NOT NULL REFERENCES "tempRoute"(id)
);

CREATE TABLE "user_class" (
    user_id UUID REFERENCES "user"(id),
    class_id UUID REFERENCES "class"(id),
    PRIMARY KEY(user_id, class_id)
);

CREATE TABLE "class_room" (
    class_id UUID REFERENCES "class"(id),
    room_id UUID REFERENCES "room"(id),
    PRIMARY KEY(class_id, room_id)
);
