Átomos: Máxima flexibilidad. Son bloques de construcción abstractos configurables con props.

Moléculas: Rígidas en su propósito, flexibles en su configuración. Tienen una identidad funcional clara, pero se adaptan con props.

Organismos: Rígidos en su layout, flexibles en sus datos. Definen las grandes secciones de tu UI, pero su contenido es dinámico y depende del estado y los datos que reciben.

Buenas Prácticas para los Átomos Pre-configurados
Hazlo por Repetición y Semántica: Crea un átomo derivado cuando una combinación de estilos se repite mucho o cuando tiene un significado de negocio muy claro (como "Botón de Eliminar").

No te excedas: No necesitas crear un componente para cada posible combinación (<SmallPrimaryButton>, <LargeSecondaryButton>). El objetivo es crear atajos para los casos de uso más comunes. Para las combinaciones raras o de un solo uso, sigue usando el átomo <Button> base.

Agrúpalos Lógicamente: Tener archivos como ActionButtons.tsx o Typography.tsx (para tus Spans) es una excelente manera de mantener tu código organizado.