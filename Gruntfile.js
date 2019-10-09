 const sass = require('node-sass');

module.exports = function(grunt) {
    require('load-grunt-tasks')(grunt);
    grunt.initConfig({
        sass: {
            options: {
                implementation: sass,
                sourceMap: true
            },
            dist: {
                files: {
                    'home/static/assets/css/style.css' : 'home/static/assets/scss/style.scss',
                }
            }
        },
        watch: {
            css: {
                files: [
                    "home/static/assets/scss/*.scss",
                    "home/static/assets/scss/**/*.scss"
                ],
                tasks: ['sass'],
                options: {
                    livereload: true,
                }
            },
            html: {
                files: ["**/templates/*.html",
                		"**/templates/**/*.html"
                ],
                options: {
                    livereload: true,
                }
            },
            js: {
                files: "js/*.js",
                options: {
                    livereload: true,
                }
            }
        }
    });
}