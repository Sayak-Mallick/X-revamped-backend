class ApiError extends Error {
  public statusCode: number;
  public data: null;
  public success: boolean;
  public error: unknown[];
  
  constructor(statusCode: number, message: string, error: unknown[] = [], stack="") {
    super(message);
    this.statusCode = statusCode;
    this.data = null;
    this.message = message;
    this.success = false;
    this.error = error;
    if (stack) {
      this.stack = stack;
    } else {
      Error.captureStackTrace(this, this.constructor);
    }
  }
}

export default ApiError;
