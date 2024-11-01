// import React from 'react';
// import '../Home.css';
// import Flag from 'react-world-flags';

// const Home = () => {
//     return (
//         <div className="home-container">
//             {/* Logo e Icone */}
//             <header className="header">
//                 <div className="logo">D</div>
//                 <div className="social-icons">
//                     <a href="#email">✉️</a>
//                     <a href="#github">🐙</a>
//                     <a href="#linkedin">🔗</a>
//                 </div>
//             </header>

//             {/* Sezione principale */}
//             <main className="main-content">
//                 <section className="welcome-section">
//                     <h1>Welcome.</h1>
//                     <p>
//                         My name is Lorenzo Mazzoccante, I'm a Full Stack Developer based in Pescara. 
//                         I have developed many types of front-ends from Intranet applications to Ecommerce platforms.
//                     </p>
//                     <p>
//                     I'm currently specializing in e-commerce and internal business systems,<br/> 
//                     with a focus on building aesthetically pleasing and intuitive interfaces. <br/>
//                     I'm passionate about creating user experiences that not only meet client expectations but are also highly functional.
//                     </p>
//                 </section>
//                 <section className="projects-section">
//                     <h2>Projects</h2>
//                     <ul className="projects-list">
//                         <li><a href="#domposer">Domposer</a></li>
//                         <li><a href="#cookiemunch">Cookiemunch</a></li>
//                         <li><a href="#screen-time-converter">Screen time converter</a></li>
//                         <li><a href="#led-multi">LED multi</a></li>
//                         <li><a href="#inline-svg">inline.svg</a></li>
//                     </ul>
//                 </section>
//             </main>

//             {/* Footer */}
//             <footer className="footer">
//                 <p>&copy; 2024 Me, Myself, I. <Flag code="it" style={{ width: 20, height: 12 }} /> <Flag code="gb" style={{ width: 20, height: 12 }} /> Tutti i diritti riservati.</p>
//             </footer>
//         </div>
//     );
// };

// export default Home;
import React, { useState, useEffect } from 'react';
import '../Home.css'; // Assicurati di creare un file CSS per gli stili

const Home = () => {
    const [overlay, setOverlay] = useState(false);

    useEffect(() => {
        const timer = setTimeout(() => {
            setOverlay(true);
        }, 5000); // 5000 millisecondi = 5 secondi

        return () => clearTimeout(timer); // Pulisci il timer quando il componente si smonta
    }, []);

    return (
        <div>
            <div className="video-container">
                <video autoPlay loop muted className="background-video">
                    <source src="/static/frontend/Welcome.mp4" type="video/mp4" />
                    Il tuo browser non supporta i video.
                </video>
            </div>
            <div className="welcome-text p-2 ">Benvenuto Welcome Bienvenido Bienvenue Willkommen Bem-vindo Добро пожаловать</div>
        </div>
    );
};

export default Home;
