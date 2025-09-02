## Atomic Design

Esta metodología se basa en la analogía de la química, dividiendo la interfaz en cinco niveles distintos:

Átomos (Atoms): Son los componentes más básicos e indivisibles de una interfaz. Piensa en ellos como los elementos HTML más simples, como un botón, un input, un label o un título. No tienen una utilidad funcional por sí solos, pero son la base de todo.

Moléculas (Molecules): Son grupos de átomos que se combinan para formar un componente funcional y reutilizable. Por ejemplo, una molécula de búsqueda podría estar formada por un átomo de input, un átomo de botón y un átomo de label.

Organismos (Organisms): Son estructuras más complejas y completas, compuestas por moléculas y/o átomos. Representan una sección de una interfaz, como una barra de navegación (header), un formulario de registro o una tarjeta de producto.

Plantillas (Templates): Son estructuras a nivel de página que organizan a los organismos en un diseño general. Se enfocan en la disposición de los componentes, pero sin el contenido real. Es el esqueleto de la página.

Páginas (Pages): Son instancias específicas de las plantillas. Aquí se inyecta el contenido real (texto, imágenes) en el esqueleto de la plantilla. Las páginas son lo que el usuario final ve.

## Composicion de los directorios 

1. * **src/components**
Esta carpeta contiene todos tus componentes de la interfaz de usuario (los átomos, moléculas, organismos, etc.). Aquí es donde vives tu Atomic Design. Estos componentes deberían ser lo más "tontos" posible, recibiendo datos y funciones a través de props y simplemente mostrando la información o emitiendo eventos.

2. * **src/services**
Esta es una carpeta clave para tu lógica no UI. Aquí pones las funciones que se comunican con APIs externas, bases de datos o cualquier otro servicio. Cada archivo dentro de esta carpeta puede representar una "entidad" o un "recurso" de tu API.


src/
├── components/
│   ├── atoms/
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   └── index.ts # que lo exporta, haciendo las importaciones más limpias.
│   │   ├── Input/
│   │   │   ├── Input.tsx
│   │   │   └── index.ts # que lo exporta, haciendo las importaciones más limpias.
│   │   └── Heading/
│   │       ├── Heading.tsx
│   │       └── index.ts # que lo exporta, haciendo las importaciones más limpias.
│   │
│   ├── molecules/
│   │   ├── SearchBar/
│   │   │   ├── SearchBar.tsx
│   │   │   └── index.ts
│   │   └── ProductCard/
│   │       ├── ProductCard.tsx
│   │       └── index.ts
│   │
│   └── organisms/
│       ├── Header/
│       │   ├── Header.tsx
│       │   └── index.ts
│       └── Footer/
│           ├── Footer.tsx
│           └── index.ts
│
├── services/
│   ├── api.ts
│   ├── products/
│   │   ├── products.service.ts
│   │   └── products.mock.ts (opcional)
│   ├── orders/
│   │   ├── orders.service.ts
│   │   └── index.ts
│   └── users/
│       ├── users.service.ts
│       └── index.ts
│
├── pages/
│   ├── HomePage.tsx
│   ├── ProductPage.tsx
│   ├── CheckoutPage.tsx
│   └── index.ts
│
├── templates/
│   ├── PageLayout/
│   │   ├── PageLayout.tsx
│   │   └── index.ts
│   └── ProductLayout/
│       ├── ProductLayout.tsx
│       └── index.ts
│
├── utils/
│   ├── formatters.ts
│   └── validators.ts
│
├── App.tsx
├── main.tsx
└── styles.css

### Explicación de las carpetas
* **components/**: Es el corazón de tu diseño atómico. La mejor práctica es crear subcarpetas para cada nivel (atoms, molecules, organisms) y dentro de estas, una carpeta para cada componente. Por ejemplo, en atoms/Button/, tendrías el componente y un archivo index.ts que lo exporta, haciendo las importaciones más limpias.

* **services/**: Aquí va toda la lógica que se comunica con APIs o maneja datos. Organízala por "recursos" o "entidades", como products, orders o users. Dentro de cada carpeta, puedes tener un servicio principal (products.service.ts) y si usas datos de prueba, puedes agregar un archivo de mock. El archivo api.ts en la raíz de services/ puede ser una buena práctica para centralizar la configuración de la conexión a tu API (por ejemplo, con Axios).

* **pages/**: Esta carpeta representa las páginas de tu aplicación. Cada archivo aquí es una vista que se renderiza con un React Router. Estas páginas se encargan de orquestar los componentes, llamar a los servicios para obtener datos y pasárselos a las plantillas y organismos.

* **templates/**: Similar a lo que describiste. Las plantillas definen la estructura general de una página. Por ejemplo, un PageLayout podría contener el Header, el Footer y un main donde se renderiza el contenido de la página actual. Las páginas usan estas plantillas.

* **utils/**: Una carpeta para funciones de utilidad que son genéricas y reutilizables en todo el proyecto, como validadores de formularios, formateadores de fechas o manipuladores de cadenas de texto. Esto evita la duplicación de código y mantiene tu lógica separada de la interfaz de usuario.

* **App.tsx y main.tsx**: Estos son los archivos principales de tu aplicación, generados por Vite. No es necesario moverlos, simplemente actúan como el punto de entrada.