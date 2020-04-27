from vpython import *

G = 6.67e-11 #constante da Gravitação Universal

#massas
mS = 1.989e30
mT = 5.972e24
mL = 7.36e22

#raios
raioSol = 6.9634e8
raioTerra = 6.371e6
raioLua = 1.7371e6

#distâncias
distanciaTS = 1.479e11
distanciaTL = 3.844e8
distanciaLS = distanciaTS+distanciaTL
centrodemassaTL = (distanciaTS*mT+distanciaLS*mL)/(mT+mL)

sol = sphere(pos=vector(0,0,0), radius=raioSol, texture='http://i.imgur.com/yoEzbtg.jpg', emissive=True)
terra = sphere(pos=vector(distanciaTS,0,0), radius=raioTerra, texture=textures.earth, make_trail=True)
lua = sphere(pos=vector(distanciaLS,0,0), radius=raioLua, texture='http://i.imgur.com/YPg4RPU.jpg', make_trail=True)

#parâmetros do ambiente
scene.camera.follow(terra) #astro que a câmera segue
scene.lights = []
luz_do_Sol = local_light(pos=vector(0,0,0), color=color.white)

#parâmetros iniciais
vTerra_e_Lua = sqrt(G*mS/centrodemassaTL) #velocidade inicial do sistema Terra-Lua
pTerra_e_Lua = vector(0,vTerra_e_Lua*(mT+mL),0) #momento inicial do sistema Terra-Lua
vLua = sqrt(G*mT/distanciaTL) #velocidade inicial da Lua
pLua = vector(0,vLua*mL,0) #momento inicial da Lua

deltaT = 2000
t = 0
#atualiza as órbitas
while True:
    rate(1000)

    rTerra_e_Lua = (terra.pos*mT+lua.pos*mL)/(mT+mL) #posição do centro de massa do sistema Terra-Lua
    rLua = lua.pos - terra.pos #posição da Lua em relação à Terra

    fTerra_e_Lua = -G*mS*(mT+mL)*rTerra_e_Lua/((mag(rTerra_e_Lua))**3)
    fLua = -G*mT*mL*rLua/((mag(rLua))**3)
    
    pTerra_e_Lua += fTerra_e_Lua*deltaT #atualiza o momento do sistema Terra-Lua
    pLua += fLua*deltaT #atualiza o momento da Lua

    terra.pos += (pTerra_e_Lua/(mT+mL))*deltaT #atualiza a posição da Terra em relação ao Sol
    lua.pos += (pTerra_e_Lua/(mT+mL))*deltaT #atualiza a posição da Lua em relação ao Sol
    lua.pos += (pLua/mL)*deltaT #atualiza a posição da Lua em relação à Terra

    t += deltaT
    