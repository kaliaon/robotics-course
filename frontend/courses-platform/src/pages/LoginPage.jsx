import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import styled from "styled-components";
import { authService } from "../services";
// import "./Login.css";

const LoginPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError("");

    try {
      const result = await authService.login(username, password);

      if (result.success) {
        navigate("/");
      } else {
        setError(result.message);
      }
    } catch (error) {
      setError("Жүйеге кіру кезінде қате пайда болды");
      console.error(error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <PageContainer>
      <ContentWrapper>
        <FormSection>
          <LogoContainer>
            <LogoText>
              Robo<SpaceText>Mentor</SpaceText>
            </LogoText>
            <LogoSubtext>Білім әлеміне қош келдіңіз</LogoSubtext>
          </LogoContainer>

          <Title>Жүйеге кіру</Title>
          <Subtitle>Оқу үшін жүйеге кіріңіз</Subtitle>

          {error && <ErrorMessage>{error}</ErrorMessage>}

          <Form onSubmit={handleSubmit}>
            <InputGroup>
              <Label>Пайдаланушы аты</Label>
              <Input
                type="text"
                placeholder="Пайдаланушы атыңызды енгізіңіз"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                disabled={isLoading}
                required
              />
            </InputGroup>

            <InputGroup>
              <Label>Құпия сөз</Label>
              <Input
                type="password"
                placeholder="Құпия сөзіңізді енгізіңіз"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                disabled={isLoading}
                required
              />
            </InputGroup>

            <RememberForgot>
              <RememberMe>
                <Checkbox type="checkbox" id="remember" disabled={isLoading} />
                <CheckboxLabel htmlFor="remember">
                  Мені есте сақтау
                </CheckboxLabel>
              </RememberMe>
              <ForgotPassword>Құпия сөзді ұмыттыңыз ба?</ForgotPassword>
            </RememberForgot>

            <Button type="submit" disabled={isLoading}>
              {isLoading ? "Жүктелуде..." : "Кіру"}
            </Button>
          </Form>

          <Footer>
            Тіркелгіңіз жоқ па? <StyledLink to="/register">Тіркелу</StyledLink>
          </Footer>
        </FormSection>

        <IllustrationSection>
          <Illustration
            src="https://img.freepik.com/free-vector/mobile-login-concept-illustration_114360-83.jpg?w=826&t=st=1687458818~exp=1687459418~hmac=373c1a3f2f9a68809eb24fd6f9ec273bcc51cc8dd46054698ad30990e34d8278"
            alt="Login illustration"
          />
        </IllustrationSection>
      </ContentWrapper>
    </PageContainer>
  );
};

export default LoginPage;

const PageContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  padding: 20px;
`;

const ContentWrapper = styled.div`
  display: flex;
  background: #1e293b;
  border-radius: 20px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
  width: 100%;
  max-width: 1000px;
  overflow: hidden;

  @media (max-width: 768px) {
    flex-direction: column-reverse;
  }
`;

const FormSection = styled.div`
  flex: 1;
  padding: 3rem;
  display: flex;
  flex-direction: column;

  @media (max-width: 768px) {
    padding: 2rem;
  }
`;

const LogoContainer = styled.div`
  margin-bottom: 2rem;
`;

const LogoText = styled.h1`
  font-size: 2.2rem;
  font-weight: 700;
  color: #0ea5e9;
  margin: 0;
`;

const SpaceText = styled.span`
  color: #06b6d4;
`;

const LogoSubtext = styled.p`
  font-size: 1rem;
  color: #94a3b8;
  margin: 0;
`;

const Title = styled.h2`
  font-size: 1.75rem;
  color: #e2e8f0;
  margin-bottom: 0.5rem;
  font-weight: 600;
`;

const Subtitle = styled.p`
  font-size: 1rem;
  color: #64748b;
  margin-bottom: 2rem;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
`;

const InputGroup = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
`;

const Label = styled.label`
  font-size: 0.875rem;
  font-weight: 500;
  color: #94a3b8;
`;

const Input = styled.input`
  padding: 0.75rem 1rem;
  border: 1px solid #334155;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.2s ease;
  background: #0f172a;
  color: #e2e8f0;

  &:focus {
    outline: none;
    border-color: #0ea5e9;
    box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.1);
  }

  &::placeholder {
    color: #64748b;
  }
`;

const RememberForgot = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
`;

const RememberMe = styled.div`
  display: flex;
  align-items: center;
  gap: 0.5rem;
`;

const Checkbox = styled.input`
  accent-color: #0ea5e9;
`;

const CheckboxLabel = styled.label`
  font-size: 0.875rem;
  color: #94a3b8;
`;

const ForgotPassword = styled.a`
  font-size: 0.875rem;
  color: #0ea5e9;
  text-decoration: none;
  cursor: pointer;

  &:hover {
    text-decoration: underline;
  }
`;

const Button = styled.button`
  background: #0ea5e9;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 0.75rem;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;

  &:hover {
    background: #0284c7;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(14, 165, 233, 0.2);
  }

  &:active {
    transform: translateY(0);
  }
`;

const Footer = styled.p`
  text-align: center;
  margin-top: 2rem;
  color: #64748b;
  font-size: 0.875rem;
`;

const StyledLink = styled(Link)`
  color: #0ea5e9;
  text-decoration: none;
  font-weight: 500;

  &:hover {
    text-decoration: underline;
  }
`;

const IllustrationSection = styled.div`
  flex: 1;
  background: #0f172a;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;

  @media (max-width: 768px) {
    display: none;
  }
`;

const Illustration = styled.img`
  max-width: 100%;
  max-height: 400px;
  object-fit: contain;
`;

const ErrorMessage = styled.div`
  color: #ef4444;
  background-color: rgba(239, 68, 68, 0.1);
  padding: 0.75rem;
  border-radius: 8px;
  border-left: 4px solid #ef4444;
  margin-bottom: 1rem;
  font-size: 0.875rem;
`;
