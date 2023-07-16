from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "cargo_types" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL
);
COMMENT ON TABLE "cargo_types" IS 'Model for cargo type.';
CREATE TABLE IF NOT EXISTS "rates" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "date" VARCHAR(10) NOT NULL,
    "rate" DOUBLE PRECISION NOT NULL,
    "cargo_id" INT NOT NULL REFERENCES "cargo_types" ("id") ON DELETE RESTRICT,
    CONSTRAINT "uid_rates_date_e58ac0" UNIQUE ("date", "cargo_id")
);
COMMENT ON TABLE "rates" IS 'Model for rate assigned to date and cargo type.';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
