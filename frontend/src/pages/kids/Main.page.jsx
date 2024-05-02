import './Main.page.scss';
import { Link } from 'react-router-dom';
import reward_animal from '@assets/svg/reward_animal.svg';
import Card from '@components/card/Card';
import Page from '@components/page/Page';
export default function KidsMainPage() {
	return (
		<Page title="Главная страница">
			<Link to="/#" className="general_kids_link">
				<Card title={'Мои награды'}>
					<img className="card_image" src={reward_animal} alt="" />
				</Card>
			</Link>
			<Link to="/train" className="general_kids_link">
				<Card title={'Мои тренировки'}>
					<span className="card_description">
						тренер оценил вашу тренировку
					</span>
				</Card>
			</Link>
			<Link to="/check-list" className="general_kids_link">
				<Card title={'Мои чек-листы'} />
			</Link>
			<Link to="/schedule" className="general_kids_link">
				<Card title={'Мои расписание на сегодня'}>
					<div className="general_kids_shedule">
						<div className="general_kids_shedule_item">
							<span className="general_kids_shedule_item_time">12:50</span>
							<span> - </span>
							<span>1 площадка,</span>
							<span>тренер - Ильина Анастасия</span>
						</div>
						<div className="general_kids_shedule_item">
							<span className="general_kids_shedule_item_time">14:50</span>
							<span> - </span>
							<span>1 площадка,</span>
							<span>тренер - Ильина Анастасия</span>
						</div>
					</div>
				</Card>
			</Link>
			<div className="">
				<form className="general_kids_form" action="#">
					<h1 className="card_header">Оставить комментарий тренеру</h1>
					<textarea className="general_kids_form_textarea"></textarea>
				</form>
				<div className="general_kids_form_btn">Отправить комментарий</div>
			</div>
		</Page>
	);
}
