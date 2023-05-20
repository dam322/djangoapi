type Rating = {
  id: number;
  title: string;
  count: number;
  percent: number;
};

type AddedByStatus = {
  yet: number;
  owned: number;
  beaten: number;
  toplay: number;
  dropped: number;
  playing: number;
};

export type Game = {
  id: number;
  slug: string;
  name: string;
  released: string;
  tba: boolean;
  background_image: string;
  rating: number;
  rating_top: number;
  ratings: Rating[];
  ratings_count: number;
  reviews_text_count: number;
  added: number;
  score: null;
  added_by_status: AddedByStatus;
};

export type RAWGJSONData = {
  count: number;
  next: string;
  previous: null;
  results: Game[];
};

