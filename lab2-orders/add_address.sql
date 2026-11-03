BEGIN;
--
-- Add field delivery_address to order
--
CREATE TABLE "new__orders_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "delivery_address" text NOT NULL, "customer_name" varchar(150) NOT NULL, "order_date" date NOT NULL, "total_amount" decimal NOT NULL, "is_paid" bool NOT NULL);
INSERT INTO "new__orders_order" ("id", "customer_name", "order_date", "total_amount", "is_paid", "delivery_address") SELECT "id", "customer_name", "order_date", "total_amount", "is_paid", '' FROM "orders_order";
DROP TABLE "orders_order";
ALTER TABLE "new__orders_order" RENAME TO "orders_order";
COMMIT;
