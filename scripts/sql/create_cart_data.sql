/*
* Copyright (c) 2023 Viviany Ribeiro <vivianyribeiro10.vr@gmail.com>
* Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
*/

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
	final_price NUMERIC,
	id_customer INTEGER,
	cart_status CHARACTER VARYING,
	CONSTRAINT cart_pkey PRIMARY KEY (id_cart),
	CONSTRAINT cart_id_customer_fkey FOREIGN KEY (id_customer)
	REFERENCES customer (id_customer)
);

CREATE SEQUENCE cartid_seq
	AS INT
	START WITH 1
	INCREMENT BY 1
	OWNED BY cart.id_cart;

CREATE TABLE cart_products (
	id_cart INTEGER NOT NULL,
	id_product INTEGER NOT NULL,
	quantity INTEGER NOT NULL
);
