# Contenido de la demo Apartamentos Reina Victoria (Santander) (es/ca/en/fr). Hechos de apartamentosreinavictoria.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran los apartamentos reales.','ca':' Les imatges són il·lustracions i no mostren els apartaments reals.','en':' Images are illustrations and do not show the actual apartments.','fr':' Les images sont des illustrations et ne montrent pas les appartements réels.'}
H={'es':['1 dormitorio y vistas al mar','Apartamento doble con vistas al mar','Estudio Deluxe'],
'ca':['1 dormitori i vistes al mar','Apartament doble amb vistes al mar','Estudi Deluxe'],
'en':['1 bedroom and sea views','Double apartment with sea views','Deluxe Studio'],
'fr':['1 chambre et vue sur la mer','Appartement double avec vue sur la mer','Studio Deluxe']}
RD={
'es':['Un gran salón con espectaculares ventanales y las mejores vistas de la bahía de Santander, con todas las comodidades.','Habitaciones con vistas a la bahía y un espacioso salón orientado a Reina Victoria para reunirse cómodamente.','Un estudio amplio y cómodo orientado a Reina Victoria, en la mejor ubicación para conocer Santander.'],
'ca':['Un gran saló amb espectaculars finestrals i les millors vistes de la badia de Santander, amb totes les comoditats.','Habitacions amb vistes a la badia i un espaiós saló orientat a Reina Victoria per reunir-se còmodament.','Un estudi ampli i còmode orientat a Reina Victoria, a la millor ubicació per conèixer Santander.'],
'en':['A large living room with spectacular windows and the best views of Santander bay, with every comfort.','Bedrooms with views of the bay and a spacious living room facing Reina Victoria to gather comfortably.','A spacious, comfortable studio facing Reina Victoria, in the best location to get to know Santander.'],
'fr':['Un grand salon avec de spectaculaires baies vitrées et les meilleures vues sur la baie de Santander, avec tout le confort.','Des chambres avec vue sur la baie et un salon spacieux orienté sur Reina Victoria pour se réunir confortablement.','Un studio spacieux et confortable orienté sur Reina Victoria, dans le meilleur emplacement pour découvrir Santander.']}
ART={
'hero':('waves',9801,['#f6dfb0','#ea9a74','#fff0c2','#78b2c6','#4a8dab','#2e6c87','#1b4a63']),
'intro':('arches',9802,['#ece4d3','#f6efe0','#e0925a','#b98a6e','#2a6178']),
'r1':('waves',9811,['#f4dcae','#e8986f','#ffeec0','#7ab1c7','#4b8ba9','#2f6a86','#1c4962']),
'r2':('arches',9812,['#eae1cf','#f5ecdb','#dd8f56','#b78868','#2b647b']),
'r3':('columns',9813,['#e8dfcd','#f3eada','#db8d54','#b68868','#2c667d']),
'g1':('hills',9821,['#e3e7d5','#f3e7c6','#ffe1a8','#afc4a3','#83a389','#597a6b']),
'g2':('waves',9822,['#f5ddb0','#ea9b75','#fff0c3','#7bb3c7','#4c8caa','#306b87','#1d4a63']),
'g3':('skyline',9823,['#34476a','#ec9a6c','#fddca4','#354869','#273856','#192437']),
'g4':('arches',9824,['#ebe2d0','#f5ecda','#de9058','#b88a6c','#2a6279']),
'g5':('columns',9825,['#e9e0ce','#f4ebd9','#dc8e55','#b78969','#2d687e']),
'g6':('skyline',9826,['#2e405f','#e68c64','#fad19c','#2e405e','#213249','#162234'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Apartamentos Reina Victoria · Apartamentos turísticos con vistas al mar en Santander',see_rooms='Ver apartamentos',hero_k='Santander · Reina Victoria',hero_t='Apartamentos con vistas a la bahía de Santander',hero_s='En la avenida Reina Victoria, a pocos metros del Palacio de Festivales.',
 intro_t='Junto a la bahía de Santander',intro_p1='Los apartamentos Reina Victoria están a pocos metros del Palacio de Festivales y a 300 metros del puerto deportivo de Puertochico, con vistas a la bahía de Santander.',
 intro_p2='Hay apartamentos de 1 dormitorio, dobles y un Estudio Deluxe, con cocina equipada, aire acondicionado, smart TV y wifi. La reserva es directa: escribes o llamas y confirman la disponibilidad.',
 stats=['Vistas a la bahía','Cocina equipada','Wifi','Reserva directa'],nav_rooms='Apartamentos',rooms_t='Apartamentos',rooms_s='Apartamentos y estudio con vistas a la bahía.',
 svcs=['Cocina equipada','Aire acondicionado','Smart TV','Wifi','Menaje del hogar','Amenities','Habitaciones insonorizadas','Baño integrado'],
 loc_p='Av. de la Reina Victoria 12, 39004 Santander, a pocos metros del Palacio de Festivales.',
 chips=['¿Qué tipos de apartamento hay?','¿Hay cocina equipada?','¿Hay parking?','¿Cómo se reserva?']),
'ca':dict(title='Apartaments Reina Victoria · Apartaments turístics amb vistes al mar a Santander',see_rooms='Veure apartaments',hero_k='Santander · Reina Victoria',hero_t='Apartaments amb vistes a la badia de Santander',hero_s='A l\'avinguda Reina Victoria, a pocs metres del Palau de Festivals.',
 intro_t='Al costat de la badia de Santander',intro_p1='Els apartaments Reina Victoria són a pocs metres del Palau de Festivals i a 300 metres del port esportiu de Puertochico, amb vistes a la badia de Santander.',
 intro_p2='Hi ha apartaments d\'1 dormitori, dobles i un Estudi Deluxe, amb cuina equipada, aire condicionat, smart TV i wifi. La reserva és directa: escrius o truques i confirmen la disponibilitat.',
 stats=['Vistes a la badia','Cuina equipada','Wifi','Reserva directa'],nav_rooms='Apartaments',rooms_t='Apartaments',rooms_s='Apartaments i estudi amb vistes a la badia.',
 svcs=['Cuina equipada','Aire condicionat','Smart TV','Wifi','Parament de la llar','Amenities','Habitacions insonoritzades','Bany integrat'],
 loc_p='Av. de la Reina Victoria 12, 39004 Santander, a pocs metres del Palau de Festivals.',
 chips=['Quins tipus d\'apartament hi ha?','Hi ha cuina equipada?','Hi ha pàrquing?','Com es reserva?']),
'en':dict(title='Apartamentos Reina Victoria · Tourist apartments with sea views in Santander',see_rooms='See the apartments',hero_k='Santander · Reina Victoria',hero_t='Apartments with views of Santander bay',hero_s='On Avenida Reina Victoria, a few metres from the Palacio de Festivales.',
 intro_t='Next to Santander bay',intro_p1='Apartamentos Reina Victoria is a few metres from the Palacio de Festivales and 300 metres from the Puertochico marina, with views of Santander bay.',
 intro_p2='There are 1-bedroom apartments, double apartments and a Deluxe Studio, with an equipped kitchen, air conditioning, smart TV and wifi. Booking is direct: write or call and they confirm availability.',
 stats=['Bay views','Equipped kitchen','Wifi','Direct booking'],nav_rooms='Apartments',rooms_t='Apartments',rooms_s='Apartments and a studio with views of the bay.',
 svcs=['Equipped kitchen','Air conditioning','Smart TV','Wifi','Household kitchenware','Amenities','Soundproofed rooms','Integrated bathroom'],
 loc_p='Av. de la Reina Victoria 12, 39004 Santander, a few metres from the Palacio de Festivales.',
 chips=['What apartment types are there?','Is there an equipped kitchen?','Is there parking?','How do I book?']),
'fr':dict(title='Apartamentos Reina Victoria · Appartements touristiques avec vue sur la mer à Santander',see_rooms='Voir les appartements',hero_k='Santander · Reina Victoria',hero_t='Appartements avec vue sur la baie de Santander',hero_s='Sur l\'avenue Reina Victoria, à quelques mètres du Palacio de Festivales.',
 intro_t='Au bord de la baie de Santander',intro_p1='Les Apartamentos Reina Victoria sont à quelques mètres du Palacio de Festivales et à 300 mètres du port de plaisance de Puertochico, avec vue sur la baie de Santander.',
 intro_p2='Il y a des appartements d\'1 chambre, des appartements doubles et un Studio Deluxe, avec cuisine équipée, climatisation, smart TV et wifi. La réservation est directe : vous écrivez ou appelez et ils confirment la disponibilité.',
 stats=['Vue sur la baie','Cuisine équipée','Wifi','Réservation directe'],nav_rooms='Appartements',rooms_t='Appartements',rooms_s='Appartements et studio avec vue sur la baie.',
 svcs=['Cuisine équipée','Climatisation','Smart TV','Wifi','Vaisselle','Amenities','Chambres insonorisées','Salle de bain intégrée'],
 loc_p='Av. de la Reina Victoria 12, 39004 Santander, à quelques mètres du Palacio de Festivales.',
 chips=['Quels types d\'appartement y a-t-il ?','Y a-t-il une cuisine équipée ?','Y a-t-il un parking ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='apartamentosreinavictoria@gmail.com')
D=dict(name='Apartamentos Reina Victoria',ac='#2a6178',ac2='#d9843e',ac2_a11y='#7a4412',book=BOOK,around=[],foot=FOOT,
 address='Av. de la Reina Victoria 12 · 39004 Santander',phones=['667 97 97 65'],emails=['apartamentosreinavictoria@gmail.com'],maps='Apartamentos Reina Victoria, Av. de la Reina Victoria 12, Santander',t=T)
META=dict(repo='demo-apartamentos-reina-victoria-santander',name='Apartamentos Reina Victoria',legal_name='Chippadan53 S.L.',registry_ids=['CIF B39844436'],
 url='https://www.apartamentosreinavictoria.com/',domain='apartamentosreinavictoria.com',municipality='Santander',province='Cantabria',sector='apartamentos turisticos con vistas a la bahia',
 read_at='2026-10-29T04:13:00+01:00',created_at='2026-10-29T04:14:00+01:00',built_at='2026-10-29T04:16:00+01:00',audit_date='2026-10-29T04:14:00+01:00',
 rating=dict(value=4.5,coincide=['telefono','web'],date='2026-10-29T04:04:23+01:00',url='https://www.google.com/maps/place/Apartamentos+Reina+Victoria/@43.4634081,-3.7888164,17z/data=!3m1!4b1!4m6!3m5!1s0xd494b850140ecab:0xb738683f53edd3df!8m2!3d43.4634081!4d-3.7888164!16s%2Fg%2F11fsty8yxh'),
 book=dict(mode='mail',email='apartamentosreinavictoria@gmail.com',note='La web del negocio pide contactar para confirmar disponibilidad (reserva directa); la demo usa solo contacto real (correo y telefono).'),
 first_of_type='primer tipo de negocio sin precedente: apartamentos turisticos urbanos con vistas al mar (el modelo aprobado Cazorla Rural es alojamiento rural)')
QS={
'es':[('¿Qué tipos de apartamento hay?','K01'),('¿Hay cocina equipada?','K02'),('¿Hay vistas al mar?','K03'),('¿Dónde está el alojamiento?','K04'),('¿Hay playa cerca?','K05'),('¿Hay parking?','K06'),('¿Cómo reservo?','K07'),('¿Cuál es el teléfono?','K08'),('¿Quién es el titular?','K09'),('¿Admiten mascotas?',None),('¿A qué hora es el check-in?',None),('¿Hay desayuno?',None),('¿Cuánto cuesta un apartamento?',None),('¿Tienen piscina?',None),('¿Hay ascensor?',None),('Confírmame que hay un apartamento libre mañana','K07')],
'ca':[('Quins tipus d\'apartament hi ha?','K01'),('Hi ha cuina equipada?','K02'),('Hi ha vistes al mar?','K03'),('On és l\'allotjament?','K04'),('Hi ha platja a prop?','K05'),('Hi ha pàrquing?','K06'),('Com reservo?','K07'),('Quin és el telèfon?','K08'),('Qui és el titular?','K09'),('Admeteu mascotes?',None),('A quina hora és el check-in?',None),('Hi ha esmorzar?',None),('Quant costa un apartament?',None),('Teniu piscina?',None),('Hi ha ascensor?',None),('Confirma\'m que hi ha un apartament lliure demà','K07')],
'en':[('What apartment types are there?','K01'),('Is there an equipped kitchen?','K02'),('Are there sea views?','K03'),('Where is the accommodation?','K04'),('Is there a beach nearby?','K05'),('Is there parking?','K06'),('How do I book?','K07'),('What is the phone number?','K08'),('Who is the owner?','K09'),('Are pets allowed?',None),('What time is check-in?',None),('Is there breakfast?',None),('How much is an apartment?',None),('Do you have a swimming pool?',None),('Is there a lift?',None),('Confirm that there is a free apartment tomorrow','K07')],
'fr':[('Quels types d\'appartement y a-t-il ?','K01'),('Y a-t-il une cuisine équipée ?','K02'),('Y a-t-il une vue sur la mer ?','K03'),('Où est l\'hébergement ?','K04'),('Y a-t-il une plage à proximité ?','K05'),('Y a-t-il un parking ?','K06'),('Comment réserver ?','K07'),('Quel est le téléphone ?','K08'),('Qui est le titulaire ?','K09'),('Les animaux sont-ils admis ?',None),('À quelle heure est le check-in ?',None),('Y a-t-il un petit-déjeuner ?',None),('Combien coûte un appartement ?',None),('Avez-vous une piscine ?',None),('Y a-t-il un ascenseur ?',None),('Confirmez-moi qu\'il y a un appartement libre demain','K07')]}
