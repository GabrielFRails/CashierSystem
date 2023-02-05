CREATE TABLE customer (
	id_customer integer,
	name CHARACTER VARYING NOT NULL,
	phone CHARACTER VARYING,
	CONSTRAINT customer_pkey PRIMARY KEY (id_customer)
);

CREATE SEQUENCE cid_seq
	AS INT
	START WITH 1
	INCREMENT BY 1
	OWNED BY customer.id_customer;

INSERT INTO customer (id_customer, name, phone)
values (nextval('cid_seq'), 'Gabriel Freitas', '62992385532'),
	(nextval('cid_seq'), 'Luiza Costa', '62992389932'),
	(nextval('cid_seq'), 'Vivi', '62992329983'),
	(nextval('cid_seq'), 'Salazar Soncerina', '62996388547');

CREATE TABLE cart (
	id_cart INTEGER NOT NULL,
	sum NUMERIC,
	discount NUMERIC,
	id_product INTEGER,
	id_customer INTEGER,
	CONSTRAINT cart_pkey PRIMARY KEY (id_cart),
	CONSTRAINT cart_id_product_fkey FOREIGN KEY (id_product)
	REFERENCES product (id_product),
	CONSTRAINT cart_id_customer_fkey FOREIGN KEY (id_customer)
	REFERENCES customer (id_customer)
);
