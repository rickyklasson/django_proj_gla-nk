/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['restaurant/templates/*.html', 'restaurant/templates/pages/*.html'],
  theme: {
    extend: {
      colors: {
        primary: '#7c0606',
      },
      transitionProperty: {
        'height': 'height',
      },
    },
  },
  plugins: [],
}
