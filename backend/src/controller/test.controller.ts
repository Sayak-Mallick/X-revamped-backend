import { Request, Response } from "express";
import ApiResponse  from "../utils/ApiResponse";
import ApiError from "../utils/ApiError";

const testController = async (req: Request, res: Response) => {
  try {
    return res.status(200).json(new ApiResponse(200, "Test route is working", null));
  } catch (error) {
    console.error("Error in test route:", error);
    const statusCode = error instanceof ApiError ? error.statusCode : 500;
    const message = error instanceof ApiError ? error.message : "Internal Server Error";
    return res.status(statusCode).json(new ApiError(statusCode, message));
  }
};

export { testController };