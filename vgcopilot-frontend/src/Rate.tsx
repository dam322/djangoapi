import { Carousel, Embla } from "@mantine/carousel";
import {
  Center,
  Grid,
  Group,
  Image,
  Rating,
  Title,
  Text,
  Stack,
} from "@mantine/core";
import { RAWGJSONData, RAWGTestJSON } from "./rawgTypes";
import { useState } from "react";
import { nanoid } from "nanoid";
import { useNavigate } from "react-router-dom";
import { recommendationsReqBoby } from "./recommendationsSharedState";
import { useSetRecoilState } from "recoil";
function Rate() {
  const rating = new Map<string, number>();
  const setReqBody = useSetRecoilState(recommendationsReqBoby);
  const [embla, setEmbla] = useState<Embla | null>(null);
  let exampleRes = Object.assign({}, RAWGTestJSON)
  const toRate = exampleRes.results.slice(0, 10).map((game) => {
    return (
      <Carousel.Slide key={nanoid()}>
        <RateComp
          title={game.name}
          img={game.background_image}
          ratingMap={rating}
          embla={embla}
          setReqBody={setReqBody}
          RAWGRes={RAWGTestJSON}
        />
      </Carousel.Slide>
    );
  });
  return (
    <Carousel draggable={true} getEmblaApi={setEmbla} h={"100%"}>
      {toRate}
    </Carousel>
  );
}

export default Rate;

interface RateProps {
  title: string;
  img: string;
  ratingMap: Map<string, number>;
  embla: Embla | null;
  setReqBody: any;
  RAWGRes: RAWGJSONData;
}
function RateComp({
  title,
  img,
  ratingMap,
  embla,
  setReqBody,
  RAWGRes,
}: RateProps) {
  const navigate = useNavigate();

  return (
    <Grid
      grow
      gutter={5}
      style={{
        height: "90vh",
        alignItems: "center",
        justifyContent: "center",
        overflowX: "hidden",
      }}
    >
      <Center onClick={(e) => e.stopPropagation()}>
        <Grid.Col span={4}>
          <Center>
            <Image radius={"md"} width={"30em"} src={img} />
          </Center>
        </Grid.Col>
        <Grid.Col span={4}>
          <Center ml={"5em"} w={"100%"}>
            <Stack>
              <Title>{title}</Title>
              {/* <Text w={"45%"}>{desc}</Text> */}
              <Rating
                count={12}
                size={"xl"}
                defaultValue={0}
                onChange={(val) => {
                  ratingMap.set(title, val);
                  embla?.scrollNext();
                  if (ratingMap.size === 10) {
                    setReqBody({
                      results: RAWGRes.results,
                      user_input: Array.from(ratingMap.entries()).map(
                        ([key, value]) => {
                          return {
                            name: key,
                            rating_user: value,
                          };
                        }
                      ),
                    });

                    navigate("/recomendations");
                  }
                  console.log(ratingMap);
                }}
              />
            </Stack>
          </Center>
        </Grid.Col>
      </Center>
    </Grid>
  );
}
