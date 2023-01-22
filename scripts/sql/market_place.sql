CREATE DATABASE market_place;

DROP TABLE if exists product_type;

CREATE TABLE product_type (
	id_type integer NOT NULL,
	description CHARACTER VARYING,
	CONSTRAINT product_type_pkey PRIMARY KEY (id_type)
);

DROP TABLE if exists product;

CREATE TABLE product (
	id_product INTEGER NOT NULL,
	cod_product CHARACTER VARYING,
	description CHARACTER VARYING,
	unit INTEGER NOT NULL,
	price NUMERIC NOT NULL,
	id_type INTEGER NOT NULL,
	CONSTRAINT product_pkey PRIMARY KEY (id_product),
	CONSTRAINT product_id_type_fkey FOREIGN KEY (id_type)
	REFERENCES product_type (id_type)
);

INSERT INTO product_type (id_type, description)
values	(001, 'beverages'),
	(002, 'cereals'),
	(003, 'canned goods'),
	(004, 'cold'),
	(005, 'cleanup');

insert into product (id_product, cod_product, description, unit, price, id_type)
values	(061, 7899999912581,'Coke 2lts', 45, 10.00, 001),
	(023, 7892568964124, 'red wine', 27, 72.99, 001),
	(152, 7895384569875, 'del valle passion fruit 1l', 93, 7.99, 001 ),
	(425, 7652301277820, 'Rice 5kg', 100, 24.99, 002),
	(423, 7412891471231, 'Feijao 1kg', 143, 8.99, 002),
	(417, 7157899871254, 'Lentil', 133, 11.99, 002),
	(221, 7012547893224, 'canned peas 250g', 207, 8.99, 003),
	(205, 7891578914582, 'Tomato Extract 300g', 212, 4.99, 003),
	(241, 7548963214587, 'green olive', 103, 12.99, 003),
	(331, 7458963215124, 'mozzarella 500g', 28, 14.99, 004),
	(314, 7896214567811, 'ham 500g', 31, 12.99, 004),
	(301, 7881227996712, 'cream cheese', 53, 17.99, 004),
	(511, 7718544698716, 'cleaning loofah', 201, 1.99, 005),
	(507, 7895214567887, 'liquid soap 500ml',108, 4.99,005),
	(504, 7885513214556, 'sanitary water 2l', 67, 12.99, 005);

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