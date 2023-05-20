import {
  Center,
  Title,
  useMantineTheme,
  Text,
  Slider,
  Grid,
  Button,
} from "@mantine/core";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function StartTest() {
  const theme = useMantineTheme();
  const navigate = useNavigate();
  axios.post("http://localhost:8000/api/1recommender/", [], {
    withCredentials: true,
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  });
  function sendForm () {
    navigate("/rate")
  }
  return (
    <Center
      mx={"auto"}
      mt={"5%"}
      mb={"10%"}
      style={{
        maxWidth: "100%",
      }}
    >
      <div>
        <Title
          order={2}
          style={{
            color: theme.colorScheme === "dark" ? theme.white : theme.black,
            fontFamily: `Fira Sans, ${theme.fontFamily}`,
          }}
          ta="center"
          mt="md"
          mb={50}
        >
          Test de perfil de videojuegos
        </Title>
        <Text
          style={{
            color: theme.colorScheme === "dark" ? theme.white : theme.black,
            fontFamily: `Fira Sans, ${theme.fontFamily}`,
            width: "50%",
            margin: "auto",
          }}
          ta="center"
          mt="md"
          mb={50}
        >
          Esta encuesta de gustos en videojuegos tiene como objetivo recolectar
          información sobre las preferencias y hábitos de juego de el
          encuestado. Los resultados de la encuesta se utilizarán para entender
          mejor las tendencias y patrones en los gustos de el jugador.
        </Text>
        <Question question="Eres más de juegos actuales (> 2020), no tan viejos (2019, 2006) o clásicos (<2005)?" />
        <Question question="Te gustan juegos en primera persona, tercera persona, de vista isométrica, vista de lado, realidad virtual?" />
        <Question question="Te gustan juegos cooperativos o de un solo jugador?
" />
        <Question question="Te gustan los juegos Indie?" />
        <Center>
          <Button mt={"5em"} size="md" onClick={sendForm}>
            Enviar
          </Button>
        </Center>
      </div>
    </Center>
  );
}

export default StartTest;

function Question({ question = "Pregunta corta" }: { question: string }) {
  const theme = useMantineTheme();

  return (
    <Grid
      grow
      gutter={5}
      mt="md"
      style={{
        width: "50%",
        margin: "auto",
        marginTop: "5%",
        height: "100%",
      }}
    >
      <Grid.Col span={5}>
        <Text
          style={{
            color: theme.colorScheme === "dark" ? theme.white : theme.black,
            fontFamily: `Fira Sans, ${theme.fontFamily}`,
          }}
        >
          {question}
        </Text>
      </Grid.Col>
      <Grid.Col span={5}>
        <Slider
          ml={"5%"}
          step={1}
          max={5}
          min={1}
          marks={[
            {
              value: 1,
              label: "1",
            },
            {
              value: 2,
              label: "2",
            },
            {
              value: 3,
              label: "3",
            },
            {
              value: 4,
              label: "4",
            },
            {
              value: 5,
              label: "5",
            },
          ]}
          size={"xl"}
          variant="gradient"
          color="purple"
        />
      </Grid.Col>
    </Grid>
  );
}
