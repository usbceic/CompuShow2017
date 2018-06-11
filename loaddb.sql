----------------------------------------------------------
--														--
--       CompuSoft - The Compushow 2017 Software	    --
--														--
----------------------------------------------------------
--														--
--		Script to load data to CompuSoft database.		--
--														--
----------------------------------------------------------

-- Load Compushow categories

DELETE FROM category CASCADE;

INSERT INTO category (name, image, description)
VALUES
	(
		'CompuAdoptado',
		'CompuAdoptado.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuBully',
		'CompuBully.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuButt',
		'CompuButt.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuCartoon',
		'CompuCartoon.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuCono',
		'CompuCono.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuLolas',
		'CompuLolas.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuFitness',
		'CompuFitness.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuGordito',
		'CompuGordito.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuLove',
		'CompuLove.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuMaster',
		'CompuMaster.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuMami',
		'CompuMami.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuPapi',
		'CompuPapi.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuPro',
		'CompuPro.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuProductista',
		'CompuProductista.jpg',
		'La que se pasó todo el concierto grabando con el iPhone X'
	),
	(
		'CompuTukky',
		'CompuTukky.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuTeam',
		'CompuTeam.jpg',
		'ANTONELLA ANTONELLA'
	),
	(
		'CompuChévere',
		'CompuChévere.jpg',
		'ANTONELLA ANTONELLA'
	)
;
