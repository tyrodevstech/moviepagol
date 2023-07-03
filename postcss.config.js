module.exports = {
    parser: "postcss-scss",
    syntax: "postcss-scss",
    plugins: {
        "postcss-preset-env": {},
        "postcss-import": {},
        "tailwindcss/nesting": {},
        tailwindcss: {},
        autoprefixer: {},
        "postcss-strip-inline-comments": {},
    },
};
