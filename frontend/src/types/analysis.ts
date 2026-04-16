export type UploadResponse = {
  file_path: string;
};

export type Graph = {
  type: string;
  column: string;
};

export type GraphResponse = {
  graphs: Graph[];
};

export type AIResponse = {
  insights: any;
  json_file: string;
};

export type Analysis = {
  id: number;
  filename: string;
  file_path: string;
  basic_analysis: any;
  statistics: any;
  missing_values: any;
  graphs: any;
  ai_insights: any;
};
