import app from "./app";
import dotenv from "dotenv";
import connnectToDB from "./config/db";

dotenv.config({
  path: "./.env",
});

const port = process.env.PORT || 4001;

connnectToDB()
  .then(() => {
    const server = app.listen(port, () => {
      console.log(`Server running on port ${port}`);
    });
    server.on("error", (error) => {
      console.error("Error starting the server:", error);
      throw error;
    });
  })
  .catch((error) => {
    console.error("Error connecting to the database:", error);
    process.exit(1);
  });
