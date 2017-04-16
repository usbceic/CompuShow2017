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
	'defaultCategoryImage.jpg'),
	
	('CompuPapi',
	'El más guapo de Computación, ese que está bueno y con el que todas quieren.',
	'defaultCategoryImage.jpg'),
	
	('CompuMami',
	'La más bella de Computación, esa que entra a la sala y todos la desean.',
	'defaultCategoryImage.jpg'),
	
	('CompuGordito',
	'Mantiene deudas altas en el cuartico y no se pela una dona.',
	'defaultCategoryImage.jpg'),
	
	('CompuAdoptado',
	'No es de la carrera pero se la pasa en la sala y sabe más de nuestras materias que nosotros mismos.',
	'defaultCategoryImage.jpg'),
	
	('CompuMaster',
	'El/La profe más respetad@ de Computación.',
	'defaultCategoryImage.jpg'),
	
	('CompuFalso',
	'Iban a ser pareja en el laboratorio y bueeh…',
	'defaultCategoryImage.jpg'),
	
	
	('CompuTeam',
	'El equipo más activo de Computación.',
	'defaultCategoryImage.jpg'),
	
	('CompuCuchi',
	'Awwwwwwww…',
	'defaultCategoryImage.jpg'),
	
	('CompuChancero',
	'Ese que no puede ver a una chama porque le empieza a caer con la “mejor” de sus labias.',
	'defaultCategoryImage.jpg'),
	
	('CompuPro',
	'Va pensum, no ha retirado nada y saca 5 en todas las materias... Quisieras ser como él.',
	'defaultCategoryImage.jpg'),
	
	('CompuFitness',
	'Tiene tanta fuerza que puede levantar los servidores del LDC.',
	'defaultCategoryImage.jpg'),
	
	('CompuLove',
	'La parejita más linda de computación.',
	'defaultCategoryImage.jpg'),
	
	('CompuChapita',
	'Se reúnen para tomar unas birras y a la primera ya no puede con su vida.',
	'defaultCategoryImage.jpg'),
	
	('CompuTukky',
	'Cuando lo veas, mejor guarda el celular.',
	'defaultCategoryImage.jpg'),
	
	('CompuLolas',
	'¿Serán operadas?',
	'defaultCategoryImage.jpg'),
	
	('CompuComadre',
	'La más sociable de Computación.',
	'defaultCategoryImage.jpg'),
	
	('CompuCompadre',
	'El más sociable de Computación.',
	'defaultCategoryImage.jpg'),
	
	('CompuCartoon',
	'Ese amigo que parece que lo sacaron de la televisión.',
	'defaultCategoryImage.jpg'),
	
	('CompuProductista',
	'¿Qué es Linux? ¿Qué lenguaje es ese?',
	'defaultCategoryImage.jpg'),
	
	('CompuButt',
	'¿Será operado?',
	'defaultCategoryImage.jpg'),
	
	('CompuBully',
	'Esa persona que se la pasa burlándose de todos, basta que le digas "¡Hola!" para que haga un chiste con eso.',
	'defaultCategoryImage.jpg'),
	
	('CompuCuaima',
	'¿Quien es esa %$!* que te está escribiendo “hola hijo como estas ya comiste”? Seguro es la otra!',
	'defaultCategoryImage.jpg'),
	
	('CompuSaurio',
	'Ese amigo que ya le comienzas a ver las canas..',
	'defaultCategoryImage.jpg');