CREATE TABLE IF NOT EXISTS stock (
  sku       VARCHAR(64) PRIMARY KEY,
  available INT NOT NULL CHECK (available >= 0)
);
CREATE TABLE IF NOT EXISTS reservation (
  id              VARCHAR(36) PRIMARY KEY,
  idempotency_key VARCHAR(128) NOT NULL UNIQUE,
  sku             VARCHAR(64) NOT NULL REFERENCES stock(sku),
  quantity        INT NOT NULL,
  released        BOOLEAN NOT NULL
);
