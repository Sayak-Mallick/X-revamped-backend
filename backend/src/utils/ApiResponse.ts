class ApiResponse<T = unknown> {
  public statusCode: number;
  public data: T | null;
  public success: boolean;
  public message: string;

  constructor(statusCode: number, message: string, data: T) {
    this.statusCode = statusCode;
    this.data = data;
    this.success = statusCode >= 200 && statusCode < 400;
    this.message = message;
  }
}

export default ApiResponse;
