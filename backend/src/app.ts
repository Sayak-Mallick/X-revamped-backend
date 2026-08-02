import express from "express";
import cors from "cors";
import cookieParser from "cookie-parser";
import testRoute from "./routes/test.route";

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());
app.use(cors(
  {
    origin: process.env.CORS_ORIGIN,
    credentials: true,
  }
));

app.use("/api/v1", testRoute);

export default app;
