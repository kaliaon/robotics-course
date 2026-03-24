import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import styled from "styled-components";
import { authService } from "../services";

const Header = () => {
  const navigate = useNavigate();
  const username = sessionStorage.getItem("username");
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const handleLogout = () => {
    authService.logout();
    navigate("/login");
  };

  const toggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <HeaderWrapper>
      <HeaderContainer>
        <LogoSection>
          <LogoLink to="/">
            Robo<LogoAccent>Mentor</LogoAccent>
          </LogoLink>
        </LogoSection>

        <NavSection>
          <MobileMenuButton onClick={toggleMobileMenu}>
            <MobileMenuIcon open={mobileMenuOpen}>
              <span></span>
              <span></span>
              <span></span>
            </MobileMenuIcon>
          </MobileMenuButton>

          <NavLinks open={mobileMenuOpen}>
            <NavItem>
              <NavLink to="/">Басты бет</NavLink>
            </NavItem>
            <NavItem>
              <NavLink to="/about">Біз туралы</NavLink>
            </NavItem>
          </NavLinks>
        </NavSection>

        <UserSection>
          {username ? (
            <>
              <UserDropdown>
                <UserAvatar>{username.slice(0, 1).toUpperCase()}</UserAvatar>
                <UserMenu>
                  <UserInfo>
                    <UserName>{username}</UserName>
                    <UserRole>Студент</UserRole>
                  </UserInfo>
                  <UserMenuDivider />
                  <UserMenuItem to="/profile">
                    <MenuIcon>—</MenuIcon>
                    Менің профилім
                  </UserMenuItem>
                  <UserMenuDivider />
                  <UserMenuButton onClick={handleLogout}>
                    <MenuIcon>→</MenuIcon>
                    Шығу
                  </UserMenuButton>
                </UserMenu>
              </UserDropdown>
            </>
          ) : (
            <AuthButtons>
              <LoginButton to="/login">Кіру</LoginButton>
              <SignupButton to="/register">Тіркелу</SignupButton>
            </AuthButtons>
          )}
        </UserSection>
      </HeaderContainer>
    </HeaderWrapper>
  );
};

export default Header;

// Styled Components
const HeaderWrapper = styled.header`
  background-color: #0f172a;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  position: sticky;
  top: 0;
  z-index: 1000;
`;

const HeaderContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  max-width: 1200px;
  margin: 0 auto;
  height: 70px;

  @media (max-width: 768px) {
    position: relative;
  }
`;

const LogoSection = styled.div`
  flex: 0 0 auto;
`;

const LogoLink = styled(Link)`
  font-size: 1.5rem;
  font-weight: 800;
  color: #0ea5e9;
  text-decoration: none;
  display: flex;
  align-items: center;
`;

const LogoAccent = styled.span`
  color: #06b6d4;
`;

const NavSection = styled.nav`
  display: flex;
  align-items: center;

  @media (max-width: 768px) {
    order: 3;
    width: 100%;
  }
`;

const NavLinks = styled.ul`
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;

  @media (max-width: 768px) {
    position: absolute;
    top: 70px;
    left: 0;
    right: 0;
    flex-direction: column;
    background-color: #0f172a;
    box-shadow: 0 10px 10px rgba(0, 0, 0, 0.3);
    padding: 0;
    max-height: ${(props) => (props.open ? "300px" : "0")};
    overflow: hidden;
    transition: max-height 0.3s ease;
  }
`;

const NavItem = styled.li`
  margin: 0 15px;

  @media (max-width: 768px) {
    margin: 0;
  }
`;

const NavLink = styled(Link)`
  text-decoration: none;
  color: #94a3b8;
  font-weight: 500;
  font-size: 1rem;
  padding: 10px 0;
  display: block;
  position: relative;
  transition: color 0.2s;

  &:hover {
    color: #0ea5e9;
  }

  &:after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background-color: #0ea5e9;
    transition: width 0.3s;
  }

  &:hover:after {
    width: 100%;
  }

  @media (max-width: 768px) {
    padding: 15px 20px;

    &:after {
      display: none;
    }

    &:hover {
      background-color: #1e293b;
    }
  }
`;

const MobileMenuButton = styled.button`
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 10px;
  margin-left: auto;

  @media (max-width: 768px) {
    display: block;
  }
`;

const MobileMenuIcon = styled.div`
  width: 24px;
  height: 18px;
  position: relative;

  span {
    display: block;
    position: absolute;
    height: 2px;
    width: 100%;
    background: #94a3b8;
    border-radius: 2px;
    transition: transform 0.2s ease, opacity 0.2s ease;

    &:nth-child(1) {
      top: ${(props) => (props.open ? "8px" : "0")};
      transform: ${(props) => (props.open ? "rotate(45deg)" : "none")};
    }

    &:nth-child(2) {
      top: 8px;
      opacity: ${(props) => (props.open ? "0" : "1")};
    }

    &:nth-child(3) {
      top: ${(props) => (props.open ? "8px" : "16px")};
      transform: ${(props) => (props.open ? "rotate(-45deg)" : "none")};
    }
  }
`;

const UserSection = styled.div`
  display: flex;
  align-items: center;
`;

const AuthButtons = styled.div`
  display: flex;
  gap: 10px;
`;

const LoginButton = styled(Link)`
  padding: 8px 16px;
  color: #0ea5e9;
  border: 1px solid #0ea5e9;
  border-radius: 4px;
  font-weight: 500;
  text-decoration: none;
  transition: background-color 0.2s, color 0.2s;

  &:hover {
    background-color: #0ea5e9;
    color: white;
  }
`;

const SignupButton = styled(Link)`
  padding: 8px 16px;
  background-color: #0ea5e9;
  color: white;
  border: 1px solid #0ea5e9;
  border-radius: 4px;
  font-weight: 500;
  text-decoration: none;
  transition: background-color 0.2s;

  &:hover {
    background-color: #0284c7;
  }
`;

const UserDropdown = styled.div`
  position: relative;

  &:hover > div:last-child {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }
`;

const UserAvatar = styled.div`
  width: 40px;
  height: 40px;
  background: linear-gradient(45deg, #0ea5e9, #06b6d4);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
`;

const UserMenu = styled.div`
  position: absolute;
  top: calc(100% + 10px);
  right: 0;
  width: 220px;
  background: #1e293b;
  border-radius: 8px;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
  padding: 10px 0;
  opacity: 0;
  visibility: hidden;
  transform: translateY(10px);
  transition: opacity 0.2s, visibility 0.2s, transform 0.2s;
  z-index: 10;

  &:before {
    content: "";
    position: absolute;
    top: -6px;
    right: 17px;
    width: 12px;
    height: 12px;
    background: #1e293b;
    transform: rotate(45deg);
    box-shadow: -2px -2px 5px rgba(0, 0, 0, 0.04);
  }
`;

const UserInfo = styled.div`
  padding: 10px 15px;
  border-bottom: 1px solid #334155;
`;

const UserName = styled.div`
  font-weight: 600;
  color: #e2e8f0;
  margin-bottom: 4px;
`;

const UserRole = styled.div`
  font-size: 0.75rem;
  color: #64748b;
`;

const UserMenuDivider = styled.div`
  height: 1px;
  background-color: #334155;
  margin: 8px 0;
`;

const UserMenuItem = styled(Link)`
  display: flex;
  align-items: center;
  padding: 10px 15px;
  color: #94a3b8;
  text-decoration: none;
  transition: background-color 0.2s;
  font-size: 0.9rem;

  &:hover {
    background-color: #334155;
  }
`;

const UserMenuButton = styled.button`
  display: flex;
  align-items: center;
  width: 100%;
  padding: 10px 15px;
  color: #ef4444;
  background: none;
  border: none;
  text-align: left;
  cursor: pointer;
  transition: background-color 0.2s;
  font-size: 0.9rem;

  &:hover {
    background-color: #334155;
  }
`;

const MenuIcon = styled.span`
  margin-right: 10px;
  font-size: 16px;
  display: inline-block;
  width: 20px;
`;
