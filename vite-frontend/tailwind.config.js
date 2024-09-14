/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './components/main.tsx',   // Falls du eine index.html verwendest
    './src/**/*.{js,ts,jsx,tsx}', // Überwacht alle Dateien in src mit diesen Endungen
  ],
  theme: {
    extend: {
      spacing: {
        '1/8': '12.5%',
      }
    },
  },
  plugins: [],
}
