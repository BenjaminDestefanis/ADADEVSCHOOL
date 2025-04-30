/** @type {import('tailwindcss').Config} */
module.exports = {  // Sintaxis Node js para aexportar modulos, aqui serviria para exportar , y le indicamos a tailwinds a quien se lo va a aplicar --
    content: [
      "./index.html",
      "./src/**/*.{js,ts,jsx,tsx}", // 'patrin glob' -- en la carpeta src, y subcarpetas , en todos los archivos con extensiones indicadas
    ],
    theme: {    // Personalizamos el tema por defecto de Tailwind
      extend: {     // Esto es apropiado por asi extendemos lso valores por defecto , si no extendemos, pisariamos los valores por defecto de tailwind
        colors: {
          primary: '#4F46E5',
          secondary: '#10B981',
          dark: '#1F2937',
          light: '#F9FAFB',
        },
      },
    },
    plugins: [],
  }