import React from "react";
import styled from "styled-components";
import Header from "../components/Header";
import { Link } from "react-router-dom";

const AboutPage = () => {
  return (
    <PageWrapper>
      <Header />
      <HeroSection>
        <HeroContent>
          <BrandTitle>
            Robo<BrandAccent>Mentor</BrandAccent>
          </BrandTitle>
          <HeroTitle>Біз туралы</HeroTitle>
          <HeroSubtitle>
            Білім беру саласындағы инновациялық платформа
          </HeroSubtitle>
        </HeroContent>
      </HeroSection>

      <MainContent>
        <ContentSection>
          <SectionTitle>Біздің миссиямыз</SectionTitle>
          <SectionText>
            RoboMentor платформасы – бұл қазақстандықтарға сапалы білім беру
            материалдарын ұсыну арқылы ұлттық білім беру деңгейін арттыруға
            бағытталған инновациялық жоба. Біз әрбір адамға, мекен-жайына,
            материалдық жағдайына және басқа да факторларға қарамастан, сапалы
            білім алуға мүмкіндік беруді мақсат тұтамыз.
          </SectionText>
          <SectionText>
            Біздің пайымдауымызша, адамдардың білім алуға деген қолжетімділігі
            мен мүмкіндіктерін кеңейту – еліміздің жарқын болашағының кепілі.
            Сондықтан RoboMentor командасы оқушылар мен студенттерге, сондай-ақ өз
            білімін жетілдіргісі келетін ересектерге арналған білім беру
            бағдарламаларының ауқымды каталогын жасауға күш салып келеді.
          </SectionText>
        </ContentSection>

        <ValuesSection>
          <SectionTitle>Біздің құндылықтарымыз</SectionTitle>
          <ValuesGrid>
            <ValueCard>
              <ValueIcon>◆</ValueIcon>
              <ValueTitle>Сапа</ValueTitle>
              <ValueDescription>
                Біз ең жоғары сапалы білім беру контентін ұсынамыз, ол қатаң
                іріктелген және сарапшылармен қаралған.
              </ValueDescription>
            </ValueCard>
            <ValueCard>
              <ValueIcon>◇</ValueIcon>
              <ValueTitle>Қолжетімділік</ValueTitle>
              <ValueDescription>
                Біз әртүрлі білім алушыларға қолжетімді болу үшін материалдарды
                түрлі форматтарда ұсынамыз.
              </ValueDescription>
            </ValueCard>
            <ValueCard>
              <ValueIcon>▲</ValueIcon>
              <ValueTitle>Инновация</ValueTitle>
              <ValueDescription>
                Біз үнемі жаңа технологияларды зерттеп, оқу процесін жақсарту
                жолдарын іздестіреміз.
              </ValueDescription>
            </ValueCard>
            <ValueCard>
              <ValueIcon>⬡</ValueIcon>
              <ValueTitle>Қоғамдастық</ValueTitle>
              <ValueDescription>
                Біз білім алушылар мен оқытушылар арасындағы ынтымақтастықты
                қолдап, мықты қоғамдастық құрамыз.
              </ValueDescription>
            </ValueCard>
          </ValuesGrid>
        </ValuesSection>
      </MainContent>

      <ContactSection>
        <SectionTitle>Бізбен байланысыңыз</SectionTitle>
        <ContactInfo>
          <ContactItem>
            <ContactIcon>@</ContactIcon>
            <ContactText>info@robomentor.kz</ContactText>
          </ContactItem>
          <ContactItem>
            <ContactIcon>☏</ContactIcon>
            <ContactText>+7 (7XX) XXX-XXXX</ContactText>
          </ContactItem>
          <ContactItem>
            <ContactIcon>⌖</ContactIcon>
            <ContactText>Алматы қ., Қазақстан</ContactText>
          </ContactItem>
        </ContactInfo>
        <ContactButton>Бізге хабарласу</ContactButton>
      </ContactSection>

      <Footer>
        <FooterContent>
          <FooterBrand>
            Robo<BrandAccent>Mentor</BrandAccent>
          </FooterBrand>
          <FooterLinks>
            <FooterLink to="/about">Біз туралы</FooterLink>
            <FooterLink to="/contact">Байланыс</FooterLink>
            <FooterLink to="/terms">Қолдану шарттары</FooterLink>
            <FooterLink to="/privacy">Құпиялылық саясаты</FooterLink>
          </FooterLinks>
          <FooterCopyright>
            © {new Date().getFullYear()} RoboMentor. Барлық құқықтар қорғалған.
          </FooterCopyright>
        </FooterContent>
      </Footer>
    </PageWrapper>
  );
};

export default AboutPage;

// Styled Components
const PageWrapper = styled.div`
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: #0f172a;
`;

const HeroSection = styled.section`
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
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
  margin-bottom: 1rem;
`;

const BrandAccent = styled.span`
  color: #06b6d4;
`;

const HeroTitle = styled.h2`
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
`;

const HeroSubtitle = styled.p`
  font-size: 1.2rem;
  opacity: 0.9;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
`;

const MainContent = styled.main`
  max-width: 1200px;
  margin: 0 auto;
  padding: 60px 20px;
`;

const ContentSection = styled.section`
  margin-bottom: 60px;
  background-color: #1e293b;
  border-radius: 8px;
  padding: 40px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
`;

const SectionTitle = styled.h3`
  font-size: 2rem;
  font-weight: 700;
  color: #e2e8f0;
  margin-bottom: 1.5rem;
  text-align: center;
`;

const SectionText = styled.p`
  font-size: 1.1rem;
  line-height: 1.8;
  color: #94a3b8;
  margin-bottom: 1.5rem;
`;

const ValuesSection = styled.section`
  margin-bottom: 60px;
`;

const ValuesGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 30px;
  margin-top: 40px;
`;

const ValueCard = styled.div`
  background-color: #1e293b;
  border-radius: 8px;
  padding: 30px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  text-align: center;
  transition: transform 0.3s ease;

  &:hover {
    transform: translateY(-5px);
  }
`;

const ValueIcon = styled.div`
  font-size: 3rem;
  margin-bottom: 15px;
  color: #0ea5e9;
`;

const ValueTitle = styled.h4`
  font-size: 1.25rem;
  font-weight: 700;
  color: #e2e8f0;
  margin-bottom: 15px;
`;

const ValueDescription = styled.p`
  font-size: 0.95rem;
  line-height: 1.6;
  color: #94a3b8;
`;

const ContactSection = styled.section`
  background-color: #1e293b;
  color: white;
  padding: 80px 20px;
  text-align: center;
`;

const ContactInfo = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 40px;
  margin: 40px 0;
`;

const ContactItem = styled.div`
  display: flex;
  align-items: center;
  font-size: 1.1rem;
`;

const ContactIcon = styled.span`
  font-size: 1.5rem;
  margin-right: 10px;
`;

const ContactText = styled.span`
  color: #94a3b8;
`;

const ContactButton = styled.button`
  background-color: #0ea5e9;
  color: white;
  font-size: 1rem;
  font-weight: 600;
  padding: 12px 24px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  transition: background-color 0.2s ease;

  &:hover {
    background-color: #0284c7;
  }
`;

const Footer = styled.footer`
  background-color: #020617;
  color: white;
  padding: 40px 20px;
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
  font-weight: 800;
  margin-bottom: 20px;
`;

const FooterLinks = styled.div`
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  flex-wrap: wrap;
  justify-content: center;
`;

const FooterLink = styled(Link)`
  color: #64748b;
  text-decoration: none;
  transition: color 0.2s ease;

  &:hover {
    color: white;
  }
`;

const FooterCopyright = styled.div`
  color: #475569;
  font-size: 0.9rem;
`;
