BEGIN;
--
-- Create model Order
--
CREATE TABLE "orders_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customer_name" varchar(150) NOT NULL, "order_date" date NOT NULL, "total_amount" decimal NOT NULL, "is_paid" bool NOT NULL);
COMMIT;
