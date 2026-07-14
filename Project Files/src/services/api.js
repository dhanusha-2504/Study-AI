import axios from "axios";

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:5000";
const UPLOAD_BASE_URL = import.meta.env.VITE_UPLOAD_BASE_URL || API_BASE_URL;

const api = axios.create({
  baseURL: `${API_BASE_URL}/api`,
});

export const uploadMaterial = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return axios.post(`${UPLOAD_BASE_URL}/api/upload-material`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};

export const generateSummary = async (text) => {
  return api.post("/generate-summary", {
    text,
  });
};

export const generateFlashcards = async (text) => {
  return api.post("/generate-flashcards", {
    text,
  });
};

export const generateSchedule = (text) => {
  return api.post("/generate-schedule", {
    text,
  });
};

export const generateQuiz = async (text) => {
  return api.post("/generate-quiz", {
    text,
  });
};

export default api;
