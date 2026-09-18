<?php
/**
 * Plugin Name: Lienbang Language Switch
 * Description: Keeps the Chinese header menu stable and adds a compact English entry button.
 * Version: 1.0.0
 * Author: Lienbang TCM
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function lienbang_is_english_path() {
	$path = isset( $_SERVER['REQUEST_URI'] ) ? wp_parse_url( wp_unslash( $_SERVER['REQUEST_URI'] ), PHP_URL_PATH ) : '';
	return is_string( $path ) && 0 === strpos( $path, '/en/' );
}

function lienbang_primary_menu_html() {
	$items = array(
		array( 'label' => '首頁', 'url' => home_url( '/' ) ),
		array( 'label' => '醫療服務', 'url' => home_url( '/services/' ) ),
		array( 'label' => '醫師介紹', 'url' => home_url( '/team/' ) ),
		array( 'label' => 'LINE預約掛號', 'url' => 'https://lin.ee/UWWKmse' ),
		array( 'label' => '健康專欄', 'url' => home_url( '/health-blog/' ) ),
		array( 'label' => '客戶服務', 'url' => home_url( '/support/' ) ),
	);

	$html = '';
	foreach ( $items as $item ) {
		$current = untrailingslashit( home_url( add_query_arg( array(), wp_parse_url( $_SERVER['REQUEST_URI'], PHP_URL_PATH ) ) ) ) === untrailingslashit( $item['url'] );
		$class   = $current ? ' menu-item current-menu-item' : ' menu-item';
		$html   .= sprintf(
			'<li class="%1$s"><a href="%2$s" class="menu-link">%3$s</a></li>',
			esc_attr( trim( $class ) ),
			esc_url( $item['url'] ),
			esc_html( $item['label'] )
		);
	}

	return $html;
}

add_filter(
	'wp_nav_menu_items',
	function ( $items, $args ) {
		if ( is_admin() || lienbang_is_english_path() ) {
			return $items;
		}

		$location = isset( $args->theme_location ) ? $args->theme_location : '';
		if ( ! in_array( $location, array( 'primary', 'mobile_menu' ), true ) ) {
			return $items;
		}

		if ( false !== strpos( $items, 'LINE預約掛號' ) && false !== strpos( $items, '醫療服務' ) ) {
			return $items;
		}

		return lienbang_primary_menu_html();
	},
	999,
	2
);

add_action(
	'wp_footer',
	function () {
		if ( is_admin() || lienbang_is_english_path() ) {
			return;
		}
		?>
		<a class="lb-en-entry" href="https://lienbangtcm.tw/en/home-3/" aria-label="English version">EN</a>
		<style>
			.lb-en-entry {
				position: fixed;
				top: 18px;
				right: 18px;
				z-index: 999998;
				display: inline-flex;
				align-items: center;
				justify-content: center;
				width: 42px;
				height: 42px;
				border: 1px solid rgba(88, 64, 46, .28);
				border-radius: 999px;
				background: rgba(255, 255, 255, .94);
				color: #5d3f2e;
				font-size: 13px;
				font-weight: 700;
				letter-spacing: 0;
				line-height: 1;
				text-decoration: none;
				box-shadow: 0 6px 18px rgba(0, 0, 0, .12);
			}
			.lb-en-entry:hover,
			.lb-en-entry:focus {
				background: #8a6a45;
				border-color: #8a6a45;
				color: #fff;
				text-decoration: none;
			}
			@media (max-width: 921px) {
				.lb-en-entry {
					top: 14px;
					right: 64px;
					width: 38px;
					height: 38px;
					font-size: 12px;
				}
			}
		</style>
		<?php
	}
);
