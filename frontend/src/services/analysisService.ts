import api from "./api";
import type {
  UploadResponse,
  GraphResponse,
  AIResponse,
  Analysis,
} from "../types/analysis";

export const uploadFile = async (file: File): Promise<UploadResponse> => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await api.post("/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};

export const analyzeFile = async (file_path: string): Promise<AIResponse> => {
  const response = await api.post("/api/ai-analysis", { file_path });

  return response.data;
};

export const generateGraphs = async (
  file_path: string,
): Promise<GraphResponse> => {
  const reponse = await api.post("/api/graphs", { file_path });

  return reponse.data;
};

export const getAnalyses = async (): Promise<Analysis[]> => {
  const reponse = await api.get("/api/analyses");

  return reponse.data.analyses;
};
