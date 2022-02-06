# Grasp

##### <Slogan \/>

##### File Structure

- `src/` has all the source code. The main entrypoint is `index.ts`.
- `dist/` contains the output of the Typescript compiled code. You should not make changes to any of the files in this folder. However, if you want to compile the project from scratch you can delete this folder and run `yarn dev`.

##### Before Running

1. Install yarn with `npm install -g yarn`
2. In the project directory, run `yarn install` to install all project dependencies. You can see these dependencies on `package.json`. If this file is changed in the future, this command must be run again.
3. Run `touch .env` to create the file used to store any secret key, value, etc.

##### Running

Two ways to run the project:

- `yarn dev` runs the project and the compiler concurrently. Any edits on the `src/` directory will automatically restart the compilation and application on save.
- `yarn start` runs the project (without recompiling).
