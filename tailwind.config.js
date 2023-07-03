module.exports = {
    content: ["./templates/**/*.{html,css,js}", "./static/**/*.{html,css,js}", "node_modules/preline/dist/*.js",'index.html'],
    theme: {
        container: {
            center: true,
        },
        screens: {
            sm: "576px",
            // => @media (min-width: 640px) { ... }

            md: "768px",
            // => @media (min-width: 768px) { ... }

            lg: "992px",
            // => @media (min-width: 1024px) { ... }

            xl: "1200px",
            // => @media (min-width: 1280px) { ... }

            "2xl": "1400px",
            // => @media (min-width: 1536px) { ... }
        },
        extend: {
            fontFamily: {
                poppins: "Poppins, sans-serif",
            },
            width: {
                "col-7": "calc(14.29% - 0.5rem)",
                "col-6": "calc(16.67% - 0.5rem)",
                "col-5": "calc(20% - 0.5rem)",
                "col-4": "calc(25% - 0.5rem)",
                "col-3": "calc(33.33% - 0.5rem)",
                "col-2": "calc(50% - 0.5rem)",
            },
            colors: {
                accent: "#1976D2",
                primary: "#fafafa",
                secondary: "#171717",
                "secondary-light": "#a3a3a3",
                "secondary-lighter": "#d4d4d4",
            },
        },
    },
    darkMode: "class",
    plugins: [require("preline/plugin")],
};
