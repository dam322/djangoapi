import { Center, Grid, Image, Text, Stack } from "@mantine/core";
import { motion } from "framer-motion";
import { recommendationsReqBoby } from "./recommendationsSharedState";
import { useRecoilValue } from "recoil";
import { useEffect, useState } from "react";
import axios from "axios";
import { Game } from "./rawgTypes";
import { nanoid } from "nanoid";
function Recomendations() {
  const reqBody = useRecoilValue(recommendationsReqBoby);
  const [recommendations, setRecommendations] = useState([])
  useEffect(() => {
    console.log(reqBody);
    axios.post("https://djangoapi-production-d74d.up.railway.app/api/1recommender/", reqBody, {
      withCredentials: true,
      headers: {
        Authorization: `jwt ${localStorage.getItem("token")}`,
      },
    }).then((res) => {
      let resdata = res.data as Game[];
      const reqs = resdata.map((game) => {
        return (
          <>
            <Recomendation
              key={nanoid()}
              title={game.name}
              image={game.background_image}
            />
          </>
        );
      });
      setRecommendations(reqs as any)
    });
    return () => { };
  }, []);

  return (
    <>
      <h1 style={{textAlign: 'center', fontFamily: 'Play'}}>¡Aquí tienes tus recomendaciones, querido gamer!</h1>
      <Center h={"80%"}>
        <Grid gutter={4} justify="space-between" align="flex-start">
          {recommendations}
        </Grid>
      </Center>
    </>
  );
}

export default Recomendations;

function Recomendation({ title, image }: { title: string; image: string }) {
  return (
    <>
      <Grid.Col span={4} mb={"md"}>
        <motion.div whileHover={{ scale: 1.05 }}>
          <Stack>
            <Center>
              <Image width={"18em"} src={image} />
            </Center>
            <Center>
              <Text style={{fontFamily: 'Play'}}>{title}</Text>
            </Center>
          </Stack>
        </motion.div>
      </Grid.Col>
    </>
  );
}
