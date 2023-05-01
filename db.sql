CREATE TABLE "MyDate" (
    "id" INTEGER,
    "my_date" TEXT NOT NULL,
    "date_type" INTEGER NOT NULL DEFAULT 0 CHECK (date_type IN (-1, 0, 1, 2)),
    PRIMARY KEY ("id")
)
