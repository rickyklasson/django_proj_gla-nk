/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['restaurant/templates/*.html', 'restaurant/templates/pages/*.html', 'restaurant/templates/components/*.html'],
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
