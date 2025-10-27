// Categorías y usos del aluminio organizados por industria
const categoriasAluminio = {
    "Industria (bienes de capital y procesos)": {
        "Estructuras y automatización": [
            "Perfiles estructurales tipo T-slot (80/20)",
            "Bastidores de máquinas",
            "Mesas de trabajo",
            "Cercos de seguridad",
            "Carros y guías lineales",
            "Andamios",
            "Pasarelas y barandas industriales",
            "Plataformas y escaleras"
        ],
        "Procesos térmicos y de fluidos": [
            "Intercambiadores de calor",
            "Radiadores industriales y serpentines",
            "Aletas, placas y carcasas",
            "Conductos y plenums de HVAC",
            "Difusores y campanas de extracción",
            "Tuberías y fittings para aire comprimido",
            "Manifolds livianos y colectores"
        ],
        "Manipulación y empaque industrial": [
            "Transportadores",
            "Camas, rieles y perfiles",
            "Tolvas livianas y vibradores",
            "Mesas rotativas",
            "Bandejas, racks y contenedores retornables",
            "Pallets y jaulas plegables"
        ],
        "Equipos y componentes": [
            "Carcasas de motores y reductores",
            "Disipadores para variadores e inversores",
            "Carenados, resguardos y tapas de máquinas",
            "Gabinetes y tableros",
            "Moldes y placas para termoformado",
            "Iluminación industrial"
        ],
        "Señalización y logística interna": [
            "Postes y pórticos de señalética",
            "Flechas y tableros",
            "Cartelería de seguridad",
            "Cajas de herramientas",
            "Estuches de instrumentación"
        ]
    },
    "Transporte": {
        "Automóviles y vehículos livianos": [
            "Carrocería (capós, portones, guardabarros)",
            "Subchasis y torres de suspensión",
            "Llantas y pinzas de freno",
            "Sistemas térmicos",
            "Gestión de energía"
        ],
        "Vehículos comerciales y maquinaria móvil": [
            "Cabinas y cajas de carga",
            "Carrocerías frigoríficas",
            "Rampas y plataformas elevadoras",
            "Tanques criogénicos livianos"
        ],
        "Ferroviario": [
            "Carrocerías de coches y vagones",
            "Marcos de ventanas",
            "Bandejas portacables"
        ],
        "Aeronáutica y espacial": [
            "Fuselajes",
            "Largueros y costillas de alas",
            "Frames y paneles",
            "Carenados y racks de aviónica"
        ],
        "Naval y marina": [
            "Superestructuras",
            "Cascos de embarcaciones ligeras",
            "Mástiles y bitas",
            "Pasamanos y escaleras"
        ],
        "Micromovilidad y ciclismo": [
            "Cuadros y horquillas de bicicletas",
            "Scooters y monopatines",
            "Sillas de ruedas y andadores"
        ],
        "Infraestructura vial": [
            "Barandas y defensas livianas",
            "Postes de señalización",
            "Luminarias viales"
        ]
    },
    "Construcción y edificación": {
        "Envolvente y cerramientos": [
            "Carpinterías: marcos y hojas de ventanas",
            "Puertas y mamparas",
            "Frentes vidriados y muros cortina",
            "Fachadas ventiladas",
            "Paneles compuestos (ACM)"
        ],
        "Cubiertas y estructuras secundarias": [
            "Chapa acanalada y tejas metálicas",
            "Cumbreras y remates",
            "Canaletas y bajadas",
            "Pasarelas y escaleras"
        ],
        "Instalaciones": [
            "Bandejas portacables",
            "Canalizaciones",
            "Cajas y gabinetes eléctricos",
            "Conductos de HVAC"
        ],
        "Acabados y equipamiento": [
            "Persianas y cortinas",
            "Herrajes y manijas",
            "Mobiliario urbano",
            "Cartelería"
        ]
    },
    "Envases y embalaje": {
        "Bebidas y alimentos": [
            "Latas de bebidas y conservas",
            "Tapas y anillos",
            "Bandejas para horno",
            "Foil doméstico e industrial"
        ],
        "Farmacéutico y cuidado personal": [
            "Blísters",
            "Tubos y aerosoles"
        ],
        "Laminados multicapa": [
            "Barrera de aluminio en cartones",
            "Sobres y sachets"
        ]
    },
    "Energía y electricidad": {
        "Transmisión y distribución": [
            "Conductores ACSR/AAAC",
            "Conectores y abrazaderas",
            "Barras colectoras (busbars)"
        ],
        "Generación y almacenamiento": [
            "Marcos de módulos fotovoltaicos",
            "Estructuras de racking",
            "Carcasas de inversores y UPS",
            "Baterías Li-ion"
        ],
        "Térmico": [
            "Intercambiadores",
            "Radiadores",
            "Aletas y placas"
        ]
    },
    "Electrónica y TIC": {
        "Gestión térmica y chasis": [
            "Disipadores extruidos",
            "Heat-sinks y heat-spreaders",
            "Carcasas de notebooks y tablets",
            "Racks y bastidores"
        ],
        "Accesorios y componentes": [
            "Antenas y radomos",
            "Soportes de cámaras",
            "Cajas de sensores IoT"
        ]
    },
    "Consumo y hogar": {
        "Cocina": [
            "Ollas y sartenes",
            "Cafeteras y hervidores",
            "Utensilios varios"
        ],
        "Electrodomésticos": [
            "Interiores de heladeras",
            "Aros de ventiladores",
            "Paneles y carcasas"
        ],
        "Mobiliario y deco": [
            "Sillas y mesas plegables",
            "Estanterías livianas",
            "Marcos de cuadros"
        ]
    },
    "Salud y laboratorio": [
        "Camillas y chasis de sillas de ruedas",
        "Camas hospitalarias",
        "Bandejas de instrumental",
        "Carcasas de equipos médicos"
    ],
    "Deportes y ocio": [
        "Palos de golf",
        "Bates de béisbol",
        "Picos de trekking",
        "Equipamiento de camping",
        "Náutica recreativa"
    ],
    "Agroindustria y alimentos": [
        "Estructuras de invernaderos",
        "Cajas y bandejas para cosecha",
        "Equipos de proceso",
        "Sistemas de riego"
    ],
    "Servicios públicos e infraestructura": [
        "Postes y brazos de luminarias",
        "Carcasas de cámaras urbanas",
        "Señalética vial",
        "Puentes peatonales livianos"
    ]
};

// Función para inicializar la lista de usos
document.addEventListener('DOMContentLoaded', function() {
    const usosContainer = document.getElementById('usos-list');
    if (!usosContainer) return;

    // Iterar sobre cada categoría principal
    Object.entries(categoriasAluminio).forEach(([categoriaPrincipal, subcategorias]) => {
        // Crear contenedor de categoría principal
        const categoriaDiv = document.createElement('div');
        categoriaDiv.className = 'categoria-principal';
        categoriaDiv.style.opacity = '0';
        categoriaDiv.style.transform = 'translateY(30px)';
        categoriaDiv.style.transition = 'all 0.6s ease';

        // Título de categoría principal
        const tituloPrincipal = document.createElement('h3');
        tituloPrincipal.className = 'categoria-titulo-principal';
        tituloPrincipal.textContent = categoriaPrincipal;
        categoriaDiv.appendChild(tituloPrincipal);

        // Verificar si tiene subcategorías
        if (typeof subcategorias === 'object' && !Array.isArray(subcategorias)) {
            // Tiene subcategorías
            Object.entries(subcategorias).forEach(([subcategoria, items]) => {
                const subcategoriaDiv = document.createElement('div');
                subcategoriaDiv.className = 'subcategoria';

                const tituloSubcategoria = document.createElement('h4');
                tituloSubcategoria.className = 'subcategoria-titulo';
                tituloSubcategoria.textContent = subcategoria;
                subcategoriaDiv.appendChild(tituloSubcategoria);

                const itemsDiv = document.createElement('div');
                itemsDiv.className = 'items-container';

                items.forEach((item, index) => {
                    const itemElemento = document.createElement('div');
                    itemElemento.className = 'uso-item';
                    itemElemento.textContent = item;
                    itemElemento.style.opacity = '0';
                    itemElemento.style.transform = 'translateY(20px)';
                    itemElemento.style.transition = `all 0.4s ease ${index * 0.02}s`;
                    itemsDiv.appendChild(itemElemento);
                });

                subcategoriaDiv.appendChild(itemsDiv);
                categoriaDiv.appendChild(subcategoriaDiv);
            });
        } else {
            // No tiene subcategorías, mostrar items directamente
            const itemsDiv = document.createElement('div');
            itemsDiv.className = 'items-container';

            subcategorias.forEach((item, index) => {
                const itemElemento = document.createElement('div');
                itemElemento.className = 'uso-item';
                itemElemento.textContent = item;
                itemElemento.style.opacity = '0';
                itemElemento.style.transform = 'translateY(20px)';
                itemElemento.style.transition = `all 0.4s ease ${index * 0.02}s`;
                itemsDiv.appendChild(itemElemento);
            });

            categoriaDiv.appendChild(itemsDiv);
        }

        usosContainer.appendChild(categoriaDiv);
    });

    // Observer para detectar cuando cada categoría entra en vista
    const observerOptions = {
        threshold: 0.2,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const categoria = entry.target;
                categoria.style.opacity = '1';
                categoria.style.transform = 'translateY(0)';

                // Animar items dentro de esta categoría
                const items = categoria.querySelectorAll('.uso-item');
                items.forEach((item, itemIndex) => {
                    setTimeout(() => {
                        item.style.opacity = '1';
                        item.style.transform = 'translateY(0)';
                    }, itemIndex * 30);
                });

                // Dejar de observar esta categoría
                observer.unobserve(categoria);
            }
        });
    }, observerOptions);

    // Observar cada categoría por separado
    const categorias = usosContainer.querySelectorAll('.categoria-principal');
    categorias.forEach(categoria => {
        observer.observe(categoria);
    });
});
