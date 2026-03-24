import React, { useState, useEffect, useCallback } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Quiz from "../components/Quiz";
import styled from "styled-components";
import Header from "../components/Header";
import { courseService } from "../services";
// import { AIChatButton } from "../components/index";
import { convertToEmbedUrl, isValidYouTubeUrl } from "../utils/videoUtils";
import ReactMarkdown from "react-markdown";

const LessonPage = () => {
  const navigate = useNavigate();
  const params = useParams();
  const { lessonId } = params;

  const [data, setData] = useState();
  const [testData, setTestData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [testLoading, setTestLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchLesson = useCallback(async () => {
    try {
      setLoading(true);
      const result = await courseService.getLessonDetails(lessonId);

      if (!result.success) {
        throw new Error(
          result.message || "An error occurred while fetching lesson data"
        );
      }

      return result.data;
    } catch (error) {
      console.error(error);
      setError(error.message);

      // Check if we need to redirect to login
      const accessToken = sessionStorage.getItem("accessToken");
      if (!accessToken) {
        navigate("/login");
      }
      return null;
    } finally {
      setLoading(false);
    }
  }, [lessonId, navigate]);

  const fetchTestData = useCallback(async () => {
    if (!lessonId) return null;

    try {
      setTestLoading(true);
      const result = await courseService.getLessonTest(lessonId);

      if (!result.success) {
        console.warn("Failed to fetch test data:", result.message);
        return null;
      }

      return result.data;
    } catch (error) {
      console.error("Error fetching test data:", error);
      return null;
    } finally {
      setTestLoading(false);
    }
  }, [lessonId]);

  useEffect(() => {
    const accessToken = sessionStorage.getItem("accessToken");
    if (!accessToken) {
      navigate("/login");
      return;
    }

    fetchLesson().then((fetchedData) => {
      if (fetchedData) {
        setData(fetchedData);

        // If the lesson has a test, fetch the test data
        if (fetchedData.has_test) {
          fetchTestData().then((fetchedTestData) => {
            if (fetchedTestData) {
              setTestData(fetchedTestData);
            }
          });
        }
      }
    });
  }, [navigate, fetchLesson, fetchTestData]);

  // Handle the back button click
  const handleBackClick = () => {
    // Extract the course ID from the URL if not available directly
    const pathParts = window.location.pathname.split("/");
    const courseIndex = pathParts.indexOf("course");

    if (courseIndex !== -1 && pathParts[courseIndex + 1]) {
      // Navigate back to the course page using the course ID from the URL
      navigate(`/course/${pathParts[courseIndex + 1]}`);
    } else {
      // Fallback to just going back in history
      navigate(-1);
    }
  };

  if (loading) {
    return (
      <>
        <Header />
        <Container>
          <LoadingText>Сабақ деректері жүктелуде...</LoadingText>
        </Container>
      </>
    );
  }

  if (error) {
    return (
      <>
        <Header />
        <Container>
          <ErrorContainer>
            <ErrorText>{error}</ErrorText>
            <ErrorButton onClick={() => window.location.reload()}>
              Қайта көру
            </ErrorButton>
          </ErrorContainer>
        </Container>
      </>
    );
  }

  if (!data) {
    return (
      <>
        <Header />
        <Container>
          <Title>Сабақ деректері қолжетімді емес</Title>
        </Container>
      </>
    );
  }

  return (
    <>
      <Header />
      <Container>
        <BackButton onClick={handleBackClick}>
          <BackIcon>←</BackIcon> Курсқа оралу
        </BackButton>

        <ContentContainer>
          <Title>{data.title}</Title>
          <VideoContainer>
            <iframe
              width="900"
              height="500"
              src={convertToEmbedUrl(data.video_url)}
              title="Сабақ бейнесі"
              frameBorder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              referrerPolicy="strict-origin-when-cross-origin"
              allowFullScreen
            ></iframe>
            {!isValidYouTubeUrl(data.video_url) && (
              <VideoWarning>
                Ескерту: Бұл YouTube бейнесі емес. Кейбір функциялар жұмыс
                істемеуі мүмкін.
              </VideoWarning>
            )}
          </VideoContainer>

          {data.content && (
            <MarkdownContainer>
              <ReactMarkdown>{data.content}</ReactMarkdown>
            </MarkdownContainer>
          )}

          {data.has_test ? (
            testLoading ? (
              <QuizPlaceholder>Тест жүктелуде...</QuizPlaceholder>
            ) : testData ? (
              <Quiz quizData={testData} />
            ) : (
              <QuizPlaceholder>
                Тест деректерін жүктеу мүмкін болмады. Өтінеміз, кейінірек қайта
                көріңіз.
              </QuizPlaceholder>
            )
          ) : Array.isArray(data.quiz) && data.quiz.length > 0 ? (
            <Quiz quizData={data.quiz} />
          ) : (
            <QuizPlaceholder>
              Бұл сабақ үшін тест қолжетімді емес.
            </QuizPlaceholder>
          )}
        </ContentContainer>
        {/* <AIChatButton
          courseId={courseId}
          lessonId={lessonId}
          lessonTitle={data.title}
        /> */}
      </Container>
    </>
  );
};

export default LessonPage;

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px 20px;
  background: #0f172a;
  min-height: calc(100vh - 70px);
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
`;

const ContentContainer = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const BackButton = styled.button`
  position: absolute;
  top: 20px;
  left: 20px;
  display: flex;
  align-items: center;
  background: #1e293b;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  font-weight: 500;
  color: #0ea5e9;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.2s ease;

  &:hover {
    background: #334155;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
    transform: translateY(-1px);
  }
`;

const BackIcon = styled.span`
  margin-right: 6px;
  font-size: 18px;
`;

const Title = styled.h1`
  font-size: 2rem;
  color: #0ea5e9;
  margin-bottom: 30px;
  text-align: center;
`;

const VideoContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 40px;
  width: 100%;
  height: auto;

  iframe {
    max-width: 100%;
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  }

  @media (max-width: 980px) {
    iframe {
      width: 100%;
      height: 350px;
    }
  }

  @media (max-width: 768px) {
    iframe {
      height: 300px;
    }
  }
`;

const LoadingText = styled.p`
  font-size: 18px;
  color: #94a3b8;
  margin-top: 100px;
`;

const ErrorContainer = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 40px;
  width: 100%;
  max-width: 600px;
  margin: 80px auto;
  background: #1e293b;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
`;

const ErrorText = styled.p`
  font-size: 18px;
  color: #ff3333;
  margin-bottom: 20px;
  text-align: center;
`;

const ErrorButton = styled.button`
  padding: 10px 20px;
  background: #0ea5e9;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background 0.2s;

  &:hover {
    background: #0284c7;
  }
`;

const QuizPlaceholder = styled.div`
  width: 100%;
  max-width: 800px;
  margin-top: 20px;
  padding: 30px;
  background-color: #1e293b;
  border-radius: 10px;
  text-align: center;
  color: #94a3b8;
  font-size: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
`;

const MarkdownContainer = styled.div`
  width: 100%;
  max-width: 900px;
  margin-bottom: 40px;
  padding: 20px 30px;
  background-color: #1e293b;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  line-height: 1.8;
  color: #e2e8f0;
  font-size: 16px;

  h1, h2, h3, h4, h5, h6 {
    color: #0ea5e9;
    margin-top: 20px;
    margin-bottom: 10px;
  }

  p {
    margin-bottom: 12px;
  }

  code {
    background: #334155;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 14px;
  }

  pre {
    background: #334155;
    padding: 15px;
    border-radius: 8px;
    overflow-x: auto;
  }

  ul, ol {
    margin-left: 20px;
    margin-bottom: 12px;
  }
`;

const VideoWarning = styled.div`
  width: 100%;
  max-width: 800px;
  margin-top: 10px;
  padding: 15px;
  background-color: #fff3cd;
  border: 1px solid #ffeaa7;
  border-radius: 8px;
  text-align: center;
  color: #856404;
  font-size: 14px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
`;
