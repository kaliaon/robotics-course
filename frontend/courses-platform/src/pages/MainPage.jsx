import React, { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import styled from "styled-components";
import Header from "../components/Header";
import { courseService, authService } from "../services";

const MainPage = () => {
  const navigate = useNavigate();
  const [courses, setCourses] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const loadCourses = async () => {
      // Check authentication first
      if (!authService.isAuthenticated()) {
        navigate("/login");
        return;
      }

      try {
        setIsLoading(true);
        const result = await courseService.getAllCourses();

        if (result.success) {
          console.log("Courses data:", result.data);

          // Process the data to ensure lessons_count is available
          const processedCourses = result.data.map((course) => ({
            ...course,
            lessons_count: course.lessons?.length || 0,
          }));

          setCourses(processedCourses);
        } else {
          console.error(
            "Failed to fetch courses:",
            result.message,
            result.error
          );
          setError(result.message);
        }
      } catch (error) {
        console.error("Error in loadCourses:", error);
        setError("Курстарды жүктеу кезінде қате пайда болды");
      } finally {
        setIsLoading(false);
      }
    };

    loadCourses();
  }, [navigate]);

  return (
    <PageWrapper>
      <Header />
      <HeroSection>
        <HeroContent>
          <BrandTitle>
            Oqu<BrandAccent>Space</BrandAccent>
          </BrandTitle>
          <HeroTitle>Білім алу әлеміне қош келдіңіз</HeroTitle>
          <HeroSubtitle>
            Өзіңізді қызықтыратын курсты таңдап, жаңа дағдыларды меңгеріңіз
          </HeroSubtitle>
          <SearchContainer>
            <SearchInput type="text" placeholder="Курсты іздеу..." />
            <SearchButton>Іздеу</SearchButton>
          </SearchContainer>
        </HeroContent>
      </HeroSection>

      <MainContent>
        <SectionTitle>Курстар каталогы</SectionTitle>
        <SectionSubtitle>
          Өзіңізді қызықтыратын курсты таңдаңыз және оқуды бастаңыз
        </SectionSubtitle>

        {error && <ErrorMessage>{error}</ErrorMessage>}

        {isLoading ? (
          <LoadingContainer>
            <LoadingSpinner />
            <LoadingText>Курстар жүктелуде...</LoadingText>
          </LoadingContainer>
        ) : (
          <CoursesContainer>
            {courses.length > 0 ? (
              courses.map((course) => (
                <CourseCard key={course.id} to={`course/${course.id}`}>
                  <CourseCardImage>
                    <CourseCardImagePlaceholder />
                  </CourseCardImage>
                  <CourseCardContent>
                    <CourseCardTitle>{course.name}</CourseCardTitle>
                    <CourseCardDescription>
                      {course.description || "Курс сипаттамасы жоқ"}
                    </CourseCardDescription>
                    <CourseCardMeta>
                      <MetaItem>
                        <MetaIcon>📚</MetaIcon> {course.lessons_count || 0}{" "}
                        сабақ
                      </MetaItem>
                      <MetaItem>
                        <MetaIcon>⏱️</MetaIcon> {course.duration || "2 сағат"}
                      </MetaItem>
                    </CourseCardMeta>
                    <CourseCardButton>Курсты оқу</CourseCardButton>
                  </CourseCardContent>
                </CourseCard>
              ))
            ) : (
              <EmptyState>
                <EmptyStateIcon>📚</EmptyStateIcon>
                <EmptyStateText>Қолжетімді курстар табылмады</EmptyStateText>
                <EmptyStateSubtext>Кейінірек қайта келіңіз</EmptyStateSubtext>
              </EmptyState>
            )}
          </CoursesContainer>
        )}
      </MainContent>

      <FeaturesSection>
        <SectionTitle>Біздің платформаның артықшылықтары</SectionTitle>
        <FeaturesGrid>
          <FeatureCard>
            <FeatureIcon>🎓</FeatureIcon>
            <FeatureTitle>Сапалы білім</FeatureTitle>
            <FeatureDescription>
              Білікті оқытушылар ұсынған сапалы білім ресурстарын алыңыз
            </FeatureDescription>
          </FeatureCard>
          <FeatureCard>
            <FeatureIcon>🧠</FeatureIcon>
            <FeatureTitle>Қабылдауға ыңғайлы</FeatureTitle>
            <FeatureDescription>
              Материалдар түсінікті және меңгеруге оңай форматта берілген
            </FeatureDescription>
          </FeatureCard>
          <FeatureCard>
            <FeatureIcon>📱</FeatureIcon>
            <FeatureTitle>Қолжетімділік</FeatureTitle>
            <FeatureDescription>
              Кез келген құрылғыдан оқи аласыз - компьютер, планшет немесе
              смартфон
            </FeatureDescription>
          </FeatureCard>
          <FeatureCard>
            <FeatureIcon>🚀</FeatureIcon>
            <FeatureTitle>Тез нәтиже</FeatureTitle>
            <FeatureDescription>
              Практикалық тапсырмалар арқылы жаңа дағдыларды тез меңгересіз
            </FeatureDescription>
          </FeatureCard>
        </FeaturesGrid>
      </FeaturesSection>

      <Footer>
        <FooterContent>
          <FooterBrand>
            Oqu<BrandAccent>Space</BrandAccent>
          </FooterBrand>
          <FooterLinks>
            <FooterLink to="/about">Біз туралы</FooterLink>
            <FooterLink to="/contact">Байланыс</FooterLink>
            <FooterLink to="/terms">Қолдану шарттары</FooterLink>
            <FooterLink to="/privacy">Құпиялылық саясаты</FooterLink>
          </FooterLinks>
          <FooterCopyright>
            © {new Date().getFullYear()} OquSpace. Барлық құқықтар қорғалған.
          </FooterCopyright>
        </FooterContent>
      </Footer>
    </PageWrapper>
  );
};

export default MainPage;

// Styled Components
const PageWrapper = styled.div`
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: #f8fafc;
`;

const HeroSection = styled.section`
  background: linear-gradient(135deg, #3066be 0%, #119da4 100%);
  padding: 80px 20px;
  color: white;
  text-align: center;
`;

const HeroContent = styled.div`
  max-width: 800px;
  margin: 0 auto;
`;

const BrandTitle = styled.h1`
  font-size: 2.5rem;
  font-weight: 800;
  margin: 0 0 20px;
`;

const BrandAccent = styled.span`
  color: #8de4ff;
`;

const HeroTitle = styled.h2`
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0 0 20px;
`;

const HeroSubtitle = styled.p`
  font-size: 1.25rem;
  margin-bottom: 30px;
  opacity: 0.9;
`;

const SearchContainer = styled.div`
  display: flex;
  max-width: 600px;
  margin: 0 auto;
`;

const SearchInput = styled.input`
  flex: 1;
  padding: 15px 20px;
  border: none;
  border-radius: 8px 0 0 8px;
  font-size: 1rem;
  outline: none;
`;

const SearchButton = styled.button`
  background-color: #ff6b6b;
  color: white;
  border: none;
  border-radius: 0 8px 8px 0;
  padding: 0 30px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s;

  &:hover {
    background-color: #ff5252;
  }
`;

const MainContent = styled.main`
  padding: 60px 20px;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
`;

const SectionTitle = styled.h2`
  font-size: 2rem;
  font-weight: 700;
  color: #2d3748;
  text-align: center;
  margin: 0 0 10px;
`;

const SectionSubtitle = styled.p`
  font-size: 1.1rem;
  color: #718096;
  text-align: center;
  margin: 0 0 40px;
`;

const CoursesContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 30px;
`;

const CourseCard = styled(Link)`
  display: flex;
  flex-direction: column;
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s, box-shadow 0.3s;
  text-decoration: none;
  color: inherit;

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  }
`;

const CourseCardImage = styled.div`
  height: 180px;
  position: relative;
  overflow: hidden;
`;

const CourseCardImagePlaceholder = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, #3066be, #119da4);
`;

const CourseCardContent = styled.div`
  padding: 20px;
  flex: 1;
  display: flex;
  flex-direction: column;
`;

const CourseCardTitle = styled.h3`
  font-size: 1.25rem;
  font-weight: 600;
  color: #2d3748;
  margin: 0 0 10px;
`;

const CourseCardDescription = styled.p`
  font-size: 0.9rem;
  color: #718096;
  margin: 0 0 15px;
  flex: 1;
`;

const CourseCardMeta = styled.div`
  display: flex;
  margin-bottom: 15px;
`;

const MetaItem = styled.div`
  display: flex;
  align-items: center;
  font-size: 0.85rem;
  color: #718096;
  margin-right: 15px;
`;

const MetaIcon = styled.span`
  margin-right: 5px;
`;

const CourseCardButton = styled.span`
  background-color: #3066be;
  color: white;
  padding: 10px 0;
  border-radius: 6px;
  font-weight: 600;
  text-align: center;
  font-size: 0.9rem;
  transition: background-color 0.2s;

  &:hover {
    background-color: #254e99;
  }
`;

const LoadingContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 0;
`;

const LoadingSpinner = styled.div`
  width: 40px;
  height: 40px;
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #3066be;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
`;

const LoadingText = styled.p`
  font-size: 1.1rem;
  color: #718096;
`;

const ErrorMessage = styled.div`
  color: #e53e3e;
  background-color: #fff5f5;
  padding: 16px;
  border-radius: 8px;
  border-left: 4px solid #e53e3e;
  margin-bottom: 30px;
  font-size: 0.95rem;
`;

const EmptyState = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 0;
  grid-column: 1 / -1;
`;

const EmptyStateIcon = styled.div`
  font-size: 60px;
  margin-bottom: 20px;
`;

const EmptyStateText = styled.h3`
  font-size: 1.25rem;
  color: #2d3748;
  margin: 0 0 10px;
`;

const EmptyStateSubtext = styled.p`
  font-size: 1rem;
  color: #718096;
`;

const FeaturesSection = styled.section`
  padding: 80px 20px;
  background-color: #f1f5f9;
`;

const FeaturesGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
  max-width: 1200px;
  margin: 40px auto 0;
`;

const FeatureCard = styled.div`
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
  text-align: center;
`;

const FeatureIcon = styled.div`
  font-size: 36px;
  margin-bottom: 20px;
`;

const FeatureTitle = styled.h3`
  font-size: 1.25rem;
  font-weight: 600;
  color: #2d3748;
  margin: 0 0 15px;
`;

const FeatureDescription = styled.p`
  font-size: 0.95rem;
  color: #718096;
  margin: 0;
`;

const Footer = styled.footer`
  background-color: #2d3748;
  color: white;
  padding: 60px 20px 30px;
  margin-top: auto;
`;

const FooterContent = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const FooterBrand = styled.div`
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 30px;
`;

const FooterLinks = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 30px;
`;

const FooterLink = styled(Link)`
  color: white;
  text-decoration: none;
  margin: 0 15px 10px;
  font-size: 0.95rem;
  opacity: 0.8;
  transition: opacity 0.2s;

  &:hover {
    opacity: 1;
  }
`;

const FooterCopyright = styled.div`
  font-size: 0.85rem;
  opacity: 0.6;
`;
