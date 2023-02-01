CREATE TABLE customer (
	id_customer integer,
	name CHARACTER VARYING NOT NULL,
	phone CHARACTER VARYING,
	CONSTRAINT customer_pkey PRIMARY KEY (id_customer)
);

CREATE TABLE cart (
	id_cart INTEGER NOT NULL,
	sum NUMERIC,
	discount NUMERIC,
	id_product INTEGER,
	id_customer INTEGER,
	CONSTRAINT cart_pkey PRIMARY KEY (id_Cart),
	CONSTRAINT cart_id_product_fkey FOREIGN KEY (id_product)
	REFERENCES product (id_product),
	CONSTRAINT cart_id_customer_fkey FOREIGN KEY (id_customer)
	REFERENCES customer (id_customer);
);
