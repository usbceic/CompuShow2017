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

DELETE FROM category;

INSERT INTO category (name, description, image)
VALUES
	('CompuCono',
	'Pensándolo bien, el cono es hasta más útil que tú.',
	'CompuCono.jpg'),
	
	('CompuPapi',
	'El más guapo de Computación, ese que está bueno y con el que todas quieren.',
	'CompuPapi.jpg'),
	
	('CompuMami',
	'La más bella de Computación, esa que entra a la sala y todos la desean.',
	'CompuMami.jpg'),
	
	('CompuGordito',
	'Mantiene deudas altas en el cuartico y no se pela una dona.',
	'CompuGordito.jpg'),
	
	('CompuAdoptado',
	'No es de la carrera pero se la pasa en la sala y sabe más de nuestras materias que nosotros mismos.',
	'CompuAdoptado.jpg'),
	
	('CompuMaster',
	'El/La profe más respetad@ de Computación.',
	'CompuMaster.jpg'),
	
	('CompuFalso',
	'Iban a ser pareja en el laboratorio y bueeh…',
	'CompuFalso.jpg'),
	
	('CompuTeam',
	'El equipo más activo de Computación.',
	'CompuTeam.jpg'),
	
	('CompuCuchi',
	'Awwwwwwww…',
	'CompuCuchi.jpg'),
	
	('CompuChancero',
	'Ese que no puede ver a una chama porque le empieza a caer con la “mejor” de sus labias.',
	'CompuChancero.jpg'),
	
	('CompuPro',
	'Va pensum, no ha retirado nada y saca 5 en todas las materias... Quisieras ser como él.',
	'CompuPro.jpg'),
	
	('CompuFitness',
	'Tiene tanta fuerza que puede levantar los servidores del LDC.',
	'CompuFitness.jpg'),
	
	('CompuLove',
	'La parejita más linda de computación.',
	'CompuLove.jpg'),
	
	('CompuChapita',
	'Se reúnen para tomar unas birras y a la primera ya no puede con su vida.',
	'CompuChapita.jpg'),
	
	('CompuTukky',
	'Cuando lo veas, mejor guarda el celular.',
	'CompuTukky.jpg'),
	
	('CompuLolas',
	'¿Serán operadas?',
	'CompuLolas.jpg'),
	
	('CompuComadre',
	'La más sociable de Computación.',
	'CompuComadre.jpg'),
	
	('CompuCompadre',
	'El más sociable de Computación.',
	'CompuCompadre.jpg'),
	
	('CompuCartoon',
	'Ese amigo que parece que lo sacaron de la televisión.',
	'CompuCartoon.jpg'),
	
	('CompuProductista',
	'¿Qué es Linux? ¿Qué lenguaje es ese?',
	'CompuProductista.jpg'),
	
	('CompuButt',
	'¿Será operado?',
	'CompuButt.jpg'),
	
	('CompuBully',
	'Esa persona que se la pasa burlándose de todos, basta que le digas "¡Hola!" para que haga un chiste con eso.',
	'CompuBully.jpg'),
	
	('CompuCuaima',
	'¿Quien es esa %$!* que te está escribiendo “hola hijo como estas ya comiste”? Seguro es la otra!',
	'CompuCuaima.jpg'),
	
	('CompuSaurio',
	'Ese amigo que ya le comienzas a ver las canas..',
	'CompuSaurio.jpg');