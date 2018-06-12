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
		'El que pensó que esto era un festival de Rammstein y Linkin Park'
	),
	(
		'CompuBully',
		'CompuBully.jpg',
		'Te fastidia por ir a Coachella por farandulear cuando en realidad vas por los artistas'
	),
	(
		'CompuButt',
		'CompuButt.jpg',
		'Estamos en el desierto, no hay que desperdiciar los shorts'
	),
	(
		'CompuCartoon',
		'CompuCartoon.jpg',
		'Ese amigo que parece que lo sacaron de la televisión.'
	),
	(
		'CompuCono',
		'CompuCono.jpg',
		'Sip, es el cono del parking lot'
	),
	(
		'CompuLolas',
		'CompuLolas.jpg',
		'Si comienza a saltar los drops son más fuertes que los de Guetta'
	),
	(
		'CompuFitness',
		'CompuFitness.jpg',
		'Aprovecha el calor para mostrar los bíceps'
	),
	(
		'CompuGordito',
		'CompuGordito.jpg',
		'Pensó que Coachella era una de feria foodtrucks de pulled pork'
	),
	(
		'CompuLove',
		'CompuLove.jpg',
		'Son la envidia hasta de Vanessa Hudgens y Austin Butler'
	),
	(
		'CompuMaster',
		'CompuMaster.jpg',
		'Decepcionado porque Coachella nunca será Woodstock del 69'
	),
	(
		'CompuMami',
		'CompuMami.jpg',
		'Se roba la atención de todos, así Dua Lipa se esté presentando'
	),
	(
		'CompuPapi',
		'CompuPapi.jpg',
		'Estamos claros que va al festival a buscar culish'
	),
	(
		'CompuPro',
		'CompuPro.jpg',
		'Aquel que aguanta todo el festival'
	),
	(
		'CompuProductista',
		'CompuProductista.jpg',
		'La que se pasó todo el concierto grabando con el iPhone X'
	),
	(
		'CompuTukky',
		'CompuTukky.jpg',
		'El que va sólo para ver a BadBunny'
	),
	(
		'CompuTeam',
		'CompuTeam.jpg',
		'#SquadGoals'
	),
	(
		'CompuChévere',
		'CompuChévere.jpg',
		'El que se cuela en la foto y terminan siendo mejores amigos'
	)
;
