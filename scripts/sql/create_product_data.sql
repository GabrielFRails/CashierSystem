/*
* Copyright (c) 2023 Viviany Ribeiro <vivianyribeiro10.vr@gmail.com>
* Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
*/

DROP TABLE if exists product_type;

CREATE TABLE product_type (
	id_type INTEGER NOT NULL,
	description CHARACTER VARYING,
	CONSTRAINT product_id_type_pkey PRIMARY KEY (id_type)
);

CREATE SEQUENCE ptid_seq
	AS INT
	START WITH 1
	INCREMENT BY 1
	OWNED BY product_type.id_type;

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
		ON DELETE CASCADE
);

CREATE SEQUENCE pid_seq
	AS INT
	START WITH 1
	INCREMENT BY 1
	OWNED BY product.id_product;

INSERT INTO product_type (id_type, description)
values	(nextval('ptid_seq'), 'Beverages'),
		(nextval('ptid_seq'), 'Cereals'),
		(nextval('ptid_seq'), 'Canned goods'),
		(nextval('ptid_seq'), 'Cold'),
		(nextval('ptid_seq'), 'Cleanup');

INSERT INTO product (id_product, cod_product, description, unit, price, id_type)
values	(nextval('pid_seq'), 7899999912581,'Coke 2lts', 45, 10.00, 1),
	(nextval('pid_seq'), 7892568964124, 'Red wine', 27, 72.99, 1),
	(nextval('pid_seq'), 7895384569875, 'Del valle passion fruit 1l', 93, 7.99, 1 ),
	(nextval('pid_seq'), 7652301277820, 'Rice 5kg', 100, 24.99, 2),
	(nextval('pid_seq'), 7412891471231, 'Feijao 1kg', 143, 8.99, 2),
	(nextval('pid_seq'), 7157899871254, 'Lentil', 133, 11.99, 2),
	(nextval('pid_seq'), 7012547893224, 'Canned peas 250g', 207, 8.99, 3),
	(nextval('pid_seq'), 7891578914582, 'Tomato Extract 300g', 212, 4.99, 3),
	(nextval('pid_seq'), 7548963214587, 'Green olive', 103, 12.99, 3),
	(nextval('pid_seq'), 7458963215124, 'Mozzarella 500g', 28, 14.99, 4),
	(nextval('pid_seq'), 7896214567811, 'Ham 500g', 31, 12.99, 4),
	(nextval('pid_seq'), 7881227996712, 'Cream cheese', 53, 17.99, 4),
	(nextval('pid_seq'), 7718544698716, 'Cleaning loofah', 201, 1.99, 5),
	(nextval('pid_seq'), 7895214567887, 'Liquid soap 500ml',108, 4.99,5),
	(nextval('pid_seq'), 7885513214556, 'Sanitary water 2l', 67, 12.99, 5);
