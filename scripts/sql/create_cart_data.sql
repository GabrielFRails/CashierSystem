CREATE TABLE cart (
	id_cart INTEGER NOT NULL,
	sum NUMERIC,
	discount NUMERIC,
	id_product INTEGER,
	CONSTRAINT cart_pkey PRIMARY KEY (id_Cart),
	CONSTRAINT cart_id_product_fkey FOREIGN KEY (id_product)
	REFERENCES product (id_product)
);

CREATE TABLE customer (
	id_customer integer,
	name CHARACTER VARYING NOT NULL,
	phone CHARACTER VARYING,
	id_cart INTEGER NOT NULL,
	CONSTRAINT customer_pkey PRIMARY KEY (id_customer),
	CONSTRAINT customer_id_cart_fkey FOREIGN KEY (id_cart)
	REFERENCES cart (id_cart)
);

ALTER TABLE cart
	ADD id_customer INTEGER,
	ADD CONSTRAINT cart_id_customer_fkey FOREIGN KEY (id_customer)
	REFERENCES customer (id_customer);